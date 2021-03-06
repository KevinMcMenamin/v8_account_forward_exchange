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


{
    'name' : 'Account Forward Exchange',
    'version' : '1.0',
    'depends' : ['base', 'board', 'account_payment', ],
    'author' : 'Solnet Solutions Ltd',
    'website': 'http://www.solnetsolutions.co.nz',
    'category' : 'Account',
    'description' : ' Account Forward Exchange ',
    'data' : ['forward_exchange_view.xml', 
              'forward_exchange_data.xml',
              'security/ir.model.access.csv',
              ],
    'update_xml': [],
    'demo' : [],
    'test' : [],
    'installable' : True,
    'active' : False,
    #"certificate" : ""
}
