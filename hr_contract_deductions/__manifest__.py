# -*- coding: utf-8 -*-
{'name': "Employee Contract Deductions ",
 'summary': """
       Multiple Deductions for employee""",
 'description': """
            Add many deductions to any employee, include in payroll and can be added via salary rule to deduct from pay
    """,
 'website': "https://www.ovextech.com",
 'email': "i",
 'author': "Muhammad Ahsan Maqbool",
 'license': "OPL-1",
 'category': 'HR',
 'version': '12',
 'images': ['static/description/Banner.png'],
 'depends': ['base', 'mail', 'hr_contract', 'hr_payroll'],
 'data': [
     'data/data.xml',
     'security/ir.model.access.csv',
     'views/hr_contract_views.xml',
 ],
 'price':7,
 'currecncy':'USD',
 'demo': []
 }
