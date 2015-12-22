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

from openerp.osv import fields, osv

class ForwardExchangeUpdate(osv.Model):

    _name = 'account_forward_exchange.forward_exchange_update'

    _columns = {'name': fields.char('Name', size = 32),
                'contract_no': fields.char('Contract Number', size = 256, required = True),
                'due_date': fields.date('Due Date', required = True),
                'rate': fields.float('Rate', digits = (18, 4), required = True),
                'fe_contract': fields.many2one('account_forward_exchange.forward_exchange', 'FE Contract'),
                }



    