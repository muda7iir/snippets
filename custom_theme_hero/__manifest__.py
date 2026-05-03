# -*- coding: utf-8 -*-
{
    'name': 'Custom Corporate Hero Snippet',
    'version': '1.1.0',
    'category': 'Website',
    'summary': 'Hero blocks and 10 animated process card snippets with sidebar options.',
    'author': 'Custom Development',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'views/snippets.xml',
        'views/process_cards.xml',
        'views/snippet_options.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'custom_theme_hero/static/src/css/s_custom_hero_animated.css',
            'custom_theme_hero/static/src/scss/process_cards.scss',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}
