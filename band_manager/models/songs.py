# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Songs(models.Model):
    _name = 'manager.songs'
    # _order = 'sequence'

    name = fields.Char(string="Name", required=True)
    version_id = fields.Many2one('manager.versions', string="Version")
    band_id = fields.Many2one('manager.bands', string="Band")
    duration = fields.Float(string="Duration")
    add_information = fields.Text(string="Additional Information")
    lyrics = fields.Text(string="Lyrics")

    sequence = fields.Integer('sequence', default=10)

