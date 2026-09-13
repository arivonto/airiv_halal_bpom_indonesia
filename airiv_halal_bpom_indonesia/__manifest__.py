# -*- coding: utf-8 -*-
{
    'name': 'Indonesia Halal BPJPH Assurance & BPOM 2D QR Compliance',
    'version': '18.0.1.0.0',
    'category': 'Inventory/Traceability',
    'summary': 'Halal Assurance System (SJPH/BPJPH), BPOM 2D Barcode Serialization, NIE Management, and Batch Recall for Odoo 18',
    'description': """
Comprehensive Halal Assurance and BPOM 2D Serialization Suite for Odoo 18 Community Edition.
Designed for Indonesian Food & Beverage (F&B), Cosmetics, Herbal/Traditional Medicine, and Pharmaceutical businesses.
Compliant with UU No. 33/2014, PP No. 39/2021 (BPJPH Halal), and BPOM 2D Barcode Serialization Regulations.

Core Capabilities:
1. Halal Assurance System (SJPH / BPJPH):
   - BPJPH Halal Certificate Management (Nomor SH, Tanggal Berlaku, Lembaga Pemeriksa Halal / LPH)
   - Halal Critical Ingredient Registry & Supplier Halal Validity Tracking
   - Halal Status tagging across Products and Finished Goods (Halal Certified, Material Check Required)
2. BPOM 2D Barcode Serialization:
   - BPOM NIE (Nomor Izin Edar) validation across categories (MD/ML Pangan, NA Kosmetik, TR Herbal, SD Suplemen, DKL Farmasi)
   - Dynamic 2D QR Code serialization string generator (<NIE>|<BATCH>|<EXP_DATE>|<SERIAL_NUMBER>)
3. End-to-End Batch Recall Engine:
   - Forward Traceability: Pinpoints all customers/delivery orders that received a specific batch
   - Backward Traceability: Identifies raw material lot origins used in production
   - Quarantine and Emergency Recall Lock for non-compliant batches
4. 100% Native Community Architecture:
   - Deep two-way integration with Odoo Stock, Product Templates, and POS
   - Zero External Server Overhead - Always Free ($0.00) under LGPL-3.
""",
    'author': 'Riv Cloud Management',
    'website': 'https://airiv.id',
    'url': 'https://github.com/arivonto/airiv_halal_bpom_indonesia/blob/18.0/static/description/index.html',
    'license': 'LGPL-3',
    'price': 0.0,
    'currency': 'EUR',
    'depends': [
        'base',
        'product',
        'stock',
        'product_expiry',
        'account',
        'airiv_os_core',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/halal_certificate_views.xml',
        'views/product_template_views.xml',
        'views/stock_lot_views.xml',
        'views/halal_bpom_menu_views.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
