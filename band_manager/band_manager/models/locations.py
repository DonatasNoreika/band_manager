# -*- coding: utf-8 -*-

from openerp import models, fields

class Locations(models.Model):
    _name = 'manager.locations'

    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Address")
