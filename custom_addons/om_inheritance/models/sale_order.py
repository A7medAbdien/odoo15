# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    confirmed_user_id = fields.Many2one(
        string='Confirmed User',
        comodel_name='res.users',
    )

    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        print('Hi, I am working!! ..................')
        self.confirmed_user_id = self.env.user.id
