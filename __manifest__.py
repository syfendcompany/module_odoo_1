{
    'name': 'Woodworking Workshop',
    'version': '1.0',
    'summary': 'Manage woodworking projects and orders',
    'description': """
        Woodworking Workshop Management:
        - Project Management
        - Material Management
        - Work Orders
        - Technical Documents
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'category': 'Manufacturing',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'project',
        'product',
        'stock',
        'mrp'
    ],
    'data': [
        # Security
        'security/woodworking_groups.xml',
        'security/ir.model.access.csv',
        
        # Views
        'views/product_views.xml',
        'views/project_views.xml',
        'views/task_views.xml',
        'views/material_views.xml',
        'views/workorder_views.xml',
        'views/menu_views.xml',
        
        # Data
        'data/woodworking_data.xml',
    ],
    'demo': [
        'demo/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}