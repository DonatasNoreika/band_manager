# -*- coding: utf-8 -*-

from openerp import models, fields

class MemberAbilities(models.Model):
    _name = 'manager.abilities'

    name = fields.Char(string="Name", required=True)
    # experience = fields.Selection([
    #     ('no', "no experience"),
    #     ('little', "little"),
    #     ('ave', "average"),
    #     ('lot', "lot"),
    #     ('pro', "professional"),
    # ], string="Experience", default='ave')
