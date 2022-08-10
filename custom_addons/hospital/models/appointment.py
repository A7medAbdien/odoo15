import string
from tokenize import String
from odoo import models, fields, api


class HospitalAppointment(models.Model):
    # that will create a table with name "hospital_appointment"
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'ref'

    patient_id = fields.Many2one('hospital.patient', 'Patient')
    appointment_time = fields.Datetime(
        string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(
        string="Booking Date", default=fields.Date.context_today)
    gender = fields.Selection(related="patient_id.gender", readonly=True)
    ref = fields.Char(string="Recreance")
    rec_computed = fields.Char(
        compute='_compute_rec_computed')

    @api.depends('patient_id')
    def _compute_rec_computed(self):
        for record in self:
            record.rec_computed = record.ref + ' Appointment'

    @ api.onchange('patient_id')
    def _onchange_patient_id(self):
        self.ref = self.patient_id.ref
