# -*- coding: utf-8 -*-

from openerp import models, fields

class Members(models.Model):
    _inherit = 'res.users'

    abilities_ids = fields.Many2many('manager.abilities', string="Abilities")
    instruments_ids = fields.Many2many('product.template', string="Instruments and Equipment")
    status = fields.Selection([
        ('free', "free member"),
        ('hired', "hired member"),
        ('full', "full member"),
    ], string="Payer Status", default='full')
    add_information = fields.Text(string="Additional Information")