# -*- coding: utf-8 -*-
{
    'name': 'EECHS KP Hero Snippet',
    'version': '1.1.0',
    'category': 'Website',
    'summary': 'Adds the EECHS KP hero banner block to the website builder.',
    'description': """
EECHS KP Hero Snippet
=====================
This module adds a fully editable, drag-and-drop "EECHS KP Hero" section
to the Odoo Website Builder's Structure section.

Fully editable via the website builder:
- Background image (click section → Set Background)
- Logo image (click logo → Replace Image)
- Navigation links (click each to edit text / URL)
- Headline text & accent color (inline edit)
- Subtitle paragraph (inline edit)
- Three CTA buttons (text, color, URL)
- Three circular trust/badge items (text, color)
- All colors via the Website Builder color palette
    """,
    'author': 'NerithonX',
    'website': 'https://nerithonx.com',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'views/snippets.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
