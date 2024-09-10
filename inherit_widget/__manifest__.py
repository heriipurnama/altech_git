{
    'name': 'Custom Char Field Focus',
    'version': '1.0',
    'depends': ['web'],
    'data': [
        'views/assets.xml',  # Asset untuk JavaScript
    ],
    'assets': {
        'web.assets_backend': [
            'inherit_widget/static/src/js/char_widget_focus.js',  # Tambahkan JS ke assets backend
        ],
    },
}
