# -*- coding: utf-8 -*-
{
    'name':
    "BirdieBox Customizations",
    'summary':
    """Odoo customizations from Bohm Technologies for BirdieBox""",
    'description':
    """
		Bohm Technologies Customizations
	""",
    'author':
    "Bohm Technologies - Cre Moore",
    'website':
    "https://www.bohmtechnologies.com",
    'category':
    'Uncategorized',
    'version':
    '1.0',
    'depends': ['repair', 'sale', 'product'],
    'data': [
        'security/ir.model.access.csv', 'views/bulk_sale.xml',
        'views/sale_order.xml', 'wizards/bulk_sale_create_wizard.xml',
        'views/report_stock_forecasted.xml', 'views/product_digital_files.xml'
    ],
    'application':
    True,
}
