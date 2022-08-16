from odoo import api, fields, models


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    appointment_id = fields.Many2one(
        string='Appointment',
        comodel_name='hospital.appointment'
    )

    reason = fields.Text(
        string='Reason',
    )

    def action_cancel(self):
        return
