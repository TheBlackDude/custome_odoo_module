# -*- coding: utf-8 -*-
{
    'name': "UNMC",

    'summary': """Managing Patients""",

    'description': """
        UNMC Module for managing patients:
            - patients registration
            - patients blood test
    """,

    'author': "eHealth Africa",
    'website': "https://www.ehealthafrica.org/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
