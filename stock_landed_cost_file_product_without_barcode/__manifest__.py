{
    'name': 'Barcode Entry on Purchase Reception',
    'version': '15.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Productos sin código de barra en expediente de compras',
    'author': 'Cecomsa SRL',
    'license': 'LGPL-3',
    'depends': ['purchase', 'stock', 'product','stock_landed_costs_file'],
    'data': [
        'views/stock_landed_cost_file_product_without_barcode_views.xml',
    ],
    
    'installable': True,
    'application': False,
}
