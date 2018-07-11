# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Setlists(models.Model):
    _name = 'manager.equipment_lists'

    name = fields.Char(string="Name", required=True)
    band_id = fields.Many2one('manager.bands', string="Band")
    instruments_ids = fields.Many2many('product.template', string='Equipment list')