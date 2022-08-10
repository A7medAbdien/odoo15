from datetime import date
from odoo import api, fields, models


class HospitalPatient(models.Model):
    # that will create a table with name "hospital_patient"
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"

    active = fields.Boolean(string="Active", default=True)
    dob = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", tracking=True, compute='_compute_age')
    # age = fields.Integer(string="Age", tracking=True, compute='_compute_age', store=True)
    # list with tubules (key,value)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    name = fields.Char(string="Name", tracking=True)
    ref = fields.Char(string="Recreance")
    appointment_id = fields.Many2one(
        'hospital.appointment', string='Appointment')

    @api.depends('dob')
    def _compute_age(self):
        print("self................", self)
        for rec in self:
            today = date.today()
            if rec.dob:
                rec.age = today.year - rec.dob.year
            else:
                rec.age = 1
