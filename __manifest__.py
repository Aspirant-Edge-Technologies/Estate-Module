# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Real Estate',
    'version' : '14.0.1.0.0',
    'author' : 'Muhammad Usman',
    'summary': 'Real estate and construction',
     'sequence': 10,
    'description': """user freindly interface for real estate""",
    'category': 'Sales',
    'website': 'https://www.odoo.com/page/billing',
    'depends' : ['base'],
    'data': ['security/ir.model.access.csv','views/estate_property_views.xml'],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
