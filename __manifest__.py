{
    'name': 'Property Management',
    'version': '1.0',
    'author': 'Ciranta It services ltd',
    'category': 'Productivity',
    'description': 'Property Management Software',
    'website': '',
    'sequence':'-10',
    'depends': ['mail','maintenance','report_xlsx',],

    'data': ['security/ir.model.access.csv',
             'data/mail_temp.xml',
             'views/property_management.xml',
             'views/apartments_management.xml',
             'views/contract.xml',
             'views/maintenance.xml',
             'report/maintenance_xlxs.xml',
             'report/report.xml',
             'report/maintenance_applied_user.xml',
             'report/maintenance_xlxs.xml',
             ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'module_type': 'official',
    'license': 'LGPL-3',

}


# security - data - wizards - views  -reports