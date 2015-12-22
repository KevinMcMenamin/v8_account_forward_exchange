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

from openerp import fields, models, api, _
from openerp.exceptions import Warning

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    _description = "Purchase Order"

    ##########################################################################################################
    #
    #- Fields
    #
    ##########################################################################################################        

    forward_exchange_contract = fields.Many2one("account_forward_exchange.forward_exchange",
                                                "Forward Exchange Contract", readonly = True,
                                                states = {"draft": [("readonly", False)]},
                                                copy = False)
    