# -*- coding: utf-8 -*-
{
    'name': 'NX Industry Housing Snippets',
    'version': '1.0.0',
    'category': 'Website',
    'summary': 'Premium website snippets for housing society websites.',
    'description': """
NX Industry Housing Snippets
=============================
Professional, fully editable website builder snippets for housing
society and cooperative society websites built on Odoo 18.

Current snippets:
- President Message Card
    """,
    'author': 'NerithonX',
    'website': 'https://nerithonx.com',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'views/snippets/nx_president_message.xml',
        'views/snippets/snippets.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'nx_industry_housing/static/src/scss/_nx_president_message.scss',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}
