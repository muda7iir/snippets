# -*- coding: utf-8 -*-
{
    'name': 'Custom Corporate Hero Snippet',
    'version': '1.0.1',
    'category': 'Website',
    'summary': 'Adds a modern hero block to the website builder.',
    'description': """
Custom Corporate Hero Snippet
==============================
Adds professionally designed, drag-and-drop Hero
snippets to the Odoo Website Builder's Structure section.
    """,
    'author': 'Custom Development',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'views/snippets.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'custom_theme_hero/static/src/css/s_custom_hero_animated.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}
