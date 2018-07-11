# -*- coding: utf-8 -*-

from openerp import models, fields

class SongVersions(models.Model):
    _name = 'manager.versions'

    name = fields.Char(string="Name", required=True)
