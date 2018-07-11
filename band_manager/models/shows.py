# -*- coding: utf-8 -*-

from openerp import models, fields

class Shows(models.Model):
    _name = 'manager.shows'

    name = fields.Char(string="Name", required=True)
    date = fields.Date(string="Date")
    location_id = fields.Many2one('manager.locations', string="Location")
    band_id = fields.Many2one('manager.bands', string="Band")
    members_ids = fields.Many2many('res.users', string="Players")
    requirements_ids = fields.Many2many('product.template', string="Instruments and Equipment")
    add_information = fields.Text(string="Additional Information")
    setlist_id = fields.Many2one('manager.setlists', string="Setlist")
    players_list_id = fields.Many2one('manager.members_lists', string="Members list")
    equipment_list_id = fields.Many2one('manager.equipment_lists', string="Requirements list")

