{
    'name': 'Atlas Prime Mercantile',
    'version': '1.1',
    'sequence': 1,
    'module_type': 'official',
    'summary': 'A customize system for Atlas Prime Mercantile',
    'author': 'GeoIworks',
    'images': [],
    'depends': [
        'base_setup',
        'web',
        'base', 
        'contacts',
        'account',
        'stock',
        'sale_management',
        'purchase'
    ],
    'data': [
        'views/menu-items.xml',
        'views/login-template.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_frontend': [
            'atlasprime/static/src/js/change_title.js',
        ],
        'web.assets_backend': [
            'atlasprime/static/src/js/change_title.js',
        ],
    },
    'license': 'LGPL-3',
}
