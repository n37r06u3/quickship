# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 RyePDX LLC (http://ryepdx.com/)
#    Copyright (C) 2004-2010 OpenERP SA (<http://www.openerp.com>)
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
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################
{
    'name': 'QuickShip',
    'version': '0.01',
    'category': 'Generic Modules/Others',
    'description': "Fastest possible shipping given a barcode scanner and a scale.",
    'author': 'RyePDX LLC',
    'website': ' http://ryepdx.com',
    'depends': ['web', 'scale_proxy', 'printer_proxy', 'shipping_api'],
    'data': ['quickship.xml'],
    'css': ['static/css/widget.css'],
    'js': ['static/js/main.js', 'static/js/widget.js'],
    'qweb': ['static/widget.xml'],
    'test': ['static/test/main.js'],
    'installable': True,
    'active': True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: