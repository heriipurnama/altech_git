{
    'name': 'Material Management',
    'version': '1.0',
    'summary': 'Module for managing materials in Odoo',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
            'views/material_views.xml',
            'views/supplier_views.xml',
            'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}
