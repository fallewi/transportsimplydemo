# -*- coding: utf-8 -*-
{
    'name': "omni_transportsimply_module",

    'summary': """
        OmniTechnical TransportSimply""",

    'description': """
        OmniTechnical TransportSimply Module
    """,

    'author': "OmniTechnical Global Solutions, Inc.",
    'website': "http://www.omnitechnical.com",

    # Categories can be used to filter modules in modules
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        # 'security/user_groups.xml',
        # 'security/security_data.xml',
        'views/views.xml',
        # 'data/account_tax.xml',
        # 'data/account.tax.csv',
    ],
    'qweb': [
         # 'static/src/xml/extend_thread_fields.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
