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
    image = fields.Image(string='Image')
    tag_ids = fields.Many2many(
        string='Tag',
        comodel_name='patient.tag'
    )

    @api.model
    def create(self, vals_list):
        print("Odoo Metes are the best",
              self.env['ir.sequence'].next_by_code('hospital.patient'))
        vals_list['ref'] = self.env['ir.sequence'].next_by_code(
            'hospital.patient')
        return super(HospitalPatient, self).create(vals_list)

    def write(self, vals):
        print('write trigger when we edit', vals)
        if not self.ref and not vals.get('ref'):
            self.ref = self.env['ir.sequence'].next_by_code(
                'hospital.patient')
        return super(HospitalPatient, self).write(vals)

    @api.depends('dob')
    def _compute_age(self):
        print("self................", self)
        for rec in self:
            today = date.today()
            if rec.dob:
                rec.age = today.year - rec.dob.year
            else:
                rec.age = 1

    def name_get(self):
        # result = []
        # for record in self:
        #     name = '[' + record.ref + '] ' + record.name
        #     result.append((record.id, name))
        # return result
        return [(record.id, "[%s] %s" % (record.ref, record.name)) for record in self]
