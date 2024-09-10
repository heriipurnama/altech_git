{
    'name': 'POS Customization',
    'version': '1.0',
    'depends': ['point_of_sale'],
    'data': [
        'views/email_template.xml',  # Email Template
    ],
    'assets': {
        'point_of_sale.assets': [
            'inherit_pos/static/src/js/pos_disable_buttons.js',
            'inherit_pos/static/src/js/pos_custom_amount_buttons.js',
            'inherit_pos/static/src/js/pos_order_email.js',
        ],
    },
}
