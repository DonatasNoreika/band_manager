# -*- coding: utf-8 -*-

from openerp import models, fields

class Instruments(models.Model):
    _inherit = 'product.template'

    owner_id = fields.Many2one('res.users', string="Owner")
    add_information = fields.Text(string="Additional Information")