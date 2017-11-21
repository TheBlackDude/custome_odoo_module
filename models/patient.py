from odoo import models, fields

class patient(models.Model):
    _name = 'unmc.patient'
    first_name = fields.Char(string="First Name.", required=True)
    last_name = fields.Char(string="Last Name.", required=True)
    age = fields.Integer(string="Age.", required=True)


class Test(models.Model):
    _name = 'unmc.test'
    test_type = fields.Char(string="Test Type.", required=True)
    result = fields.Char(string="Test Result.", required=True)
    summary = fields.Text()
    date_taken = fields.Date()
