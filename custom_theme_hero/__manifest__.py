# -*- coding: utf-8 -*-
{
    'name': 'Custom Corporate Hero Snippet',
    'version': '1.0.0',
    'category': 'Website',
    'summary': 'Adds a modern hero block to the website builder.',
    'description': """
Custom Corporate Hero Snippet
==============================
Adds a professionally designed, drag-and-drop "Home Hero"
snippet to the Odoo Website Builder's Structure section.
    """,
    'author': 'Custom Development',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'views/snippets.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
