# -*- coding: utf-8 -*-

from openerp import models, fields

class Bands(models.Model):
    _name = 'manager.bands'

    name = fields.Char(string="Name", required=True)
    style_id = fields.Many2one('manager.styles', string="Style")
    # players = fields.Many2many('res.users', string="Players")
    add_information = fields.Text(string="Additional Information")

    songs_ids = fields.One2many('manager.songs', 'band_id', 'Songs')
    rehearsals_ids = fields.One2many('manager.rehearsals', 'band_id', 'Rehearsals')
    setlists_ids = fields.One2many('manager.setlists', 'band_id', 'Setlists')
    shows_ids = fields.One2many('manager.shows', 'band_id', 'Shows')

    members_lists_ids = fields.Many2many('manager.members_lists', string="Members list")
