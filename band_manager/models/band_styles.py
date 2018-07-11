# -*- coding: utf-8 -*-

from openerp import models, fields

class BandStyles(models.Model):
    _name = 'manager.styles'

    name = fields.Char(string="Name", required=True)
