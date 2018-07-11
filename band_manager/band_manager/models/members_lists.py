# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Setlists(models.Model):
    _name = 'manager.members_lists'

    name = fields.Char(string="Name", required=True)
    band_id = fields.Many2one('manager.bands', string="Band")
    members_ids = fields.Many2many('res.users', string='Members')