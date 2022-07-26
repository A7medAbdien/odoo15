from cgi import test
import string
from odoo import api, fields, models


class HospitalPatient(models.Model):
    # that will create a table with name "hospital_patient"
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string="Name")
    ref = fields.Char(string="Recreance")
    name2 = fields.Char(string="Name2")
    age = fields.Integer(string="Age")
    # list with tubules (key,value)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], string="Gender")
    # test = self.env["product.template"].browse(23).id.name
    # testo = fields.Char(string=test)
