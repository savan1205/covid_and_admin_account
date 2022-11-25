# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Covid',
    'version' : '15.0.1.0',
    'summary': 'Covid',
    'sequence': 1,
    'description': """
Covid
====================
The specific and easy-to-use Covid system in Odoo allows you to keep track of your Covid days, even when you are not an infected. It provides an easy way to follow up on your vendors and customers.

You could use this simplified covid module in case you work during an pandamic to keep your business, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'depends' : ['website'],
    'data': [ 
        'security/ir.model.access.csv',

        'controllers/products_template.xml',

        'views/shop_product_inherit.xml',
        'views/products_view.xml',
    ],
   
    'installable': True,
    'application': True,
    'auto_install': False,
    
        
    'license': 'LGPL-3',

    
}
