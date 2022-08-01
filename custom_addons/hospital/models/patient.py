from cgi import test
from email.policy import default
import string
from odoo import api, fields, models


class HospitalPatient(models.Model):
    # that will create a table with name "hospital_patient"
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"

    active = fields.Boolean(string="Active", default=True)
    age = fields.Integer(string="Age", tracking=True)
    # list with tubules (key,value)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    name = fields.Char(string="Name", tracking=True)
    name2 = fields.Char(string="Name2")
    ref = fields.Char(string="Recreance")
