# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011- Solnet Solutions (<http://www.solnetsolutions.co.nz>). 
#    Copyright (C) 2010 OpenERP S.A. http://www.openerp.com
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from decimal import Decimal
from openerp.osv import fields, osv


class ForwardExchange(osv.Model):

    _name = 'account_forward_exchange.forward_exchange'

    _columns = {'name': fields.char('FE Number', size = 32, readonly = True),
                'contract_no': fields.char('Contract Number', size = 256, required = True),
                'contract_enter_date': fields.date('Date Contract Entered Info', required = True),
                'currency_name': fields.many2one('res.currency', 'Currency Name', required = True),
                'due_date': fields.date('Due Date', required = True),
                'rate': fields.float('Rate', digits = (18,4), required = True),
                'amount_in_foreign_currency': fields.float('Amount in foreign currency',
                                                           digits = (18, 2), required = True),
                'amount_committed_in_foreign_currency': fields.float('Amount committed in foreign currency',
                                                                     digits = (18, 2), required = False),
                'state': fields.selection([('inprogress', 'In Progress'),
                                           ('complete', 'Complete'),
                                           ('cancel', 'Cancelled')],
                                          string = 'State'),
                'forward_exchange_updates': fields.one2many('account_forward_exchange.forward_exchange_update',
                                                            'fe_contract', 'Forward Exchange Contracts'),
                'reference': fields.char('Reference', size = 128, required = False)
                }

    _defaults = {'state': 'inprogress'}
    
    def create(self, cr, uid, vals, context=None):
        """ Assign the next FE reference number. """
        nextno = self.pool.get('ir.sequence').get(cr, uid, 'forward.exchange')
        vals['name'] = nextno
        return osv.osv.create(self, cr, uid, vals, context=context)


    def compute(self, cr, uid, ids, amount, convert_to = True, round = None, context = None):  # @ReservedAssignment
        """ Convert an amount to or from the currency of a forward exchange contract..

            Converts to the passed amount to or from the currency of the contract.  In practice
            this just means multiply or divide by the rate.
    
            Note this is a little simplistic at the moment and will need to change to match
            res_currency.compute if the FEC is extended to include source currency or rounding.
    
            Rounding - this uses Decimal.quantize so pass in a decimal matching the quantize
            rounding
            
            round = Decimal('0')      - 1.654321 = 2
            round = Decimal('0.1')    - 1.654321 = 1.7
            round = Decimal('0.01')   - 1.654321 = 1.65
    
			Args:
			    ids: Internal ID of a single Forward exchange contract.
				amount: The amount to convert.
				convert_to: If true, convert to the currency amount.
				round: Decimal.quantize rounding or None for no rounding.

			Returns:
                The converted amount as a float.
			Raises:
			    ValueError if ids is not present.
		"""
        if not amount:
            return 0.0
        
        if isinstance(ids, list):
            fec_id = ids and ids[0] or None
        else:
            fec_id = ids
            
        if not fec_id:
            raise ValueError('Forward Exchange Contract compute called with missing contract')
        
        fec_item = self.browse(cr, uid, fec_id, context = context)
        
        if convert_to:
            ret_amount = amount * fec_item.rate
        else:
            ret_amount = amount / fec_item.rate

        if round:
            ret_amount = float(Decimal(str(ret_amount).quantize(Decimal(str(round)))))
        
        return ret_amount


    