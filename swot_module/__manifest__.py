# -*- coding: utf-8 -*-

# Copyright (C) 2019 BI Solutions (https://bisolutions.com.np).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "SWOT Analysis",

    'summary': """
        SWOT Analysis of Individual, Department or Company""",

    'description': """
        This module helps to automate SWOT analysis for an organization.
    """,

    'author': "BI Solutions",
    'website': "https://bisolutions.com.np",

    'category': 'Management',
    'version': '1.0',

    'depends': ['base','hr'],

    'data': [
        'security/swot_access_rules.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'report/swot_report.xml',
    ],
    'demo': [],
    'application':True,
}
