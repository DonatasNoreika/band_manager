# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Setlists(models.Model):
    _name = 'manager.setlists'

    name = fields.Char(string="Name", required=True)
    band_id = fields.Many2one('manager.bands', string="Band")
    for_rehearsal = fields.Boolean(string="For Rehearsal")
    for_show = fields.Boolean(string="For Show")
    required_duration = fields.Integer(string="Required Duration")
    real_duration = fields.Char(string="Real Duration", compute="_count_duration")
    songs_ids = fields.Many2many('manager.songs', string="Songs")
    duration_ir_percents = fields.Float(string="Duration in Percents", compute='_count_duration_in_percents')
    number_of_songs = fields.Integer(string="Number of Songs", compute="_count_songs")

    @api.depends('required_duration', 'songs_ids')
    def _count_duration_in_percents(self):
        for r in self:
            if not r.required_duration:
                r.duration_ir_percents = 0.0
            else:
                count = 0
                for s in r.songs_ids:
                    count += s.duration

                r.duration_ir_percents = 100.0 * count / r.required_duration

    @api.depends('required_duration','songs_ids')
    def _count_duration(self):
        for r in self:
            count = 0
            for i in r.songs_ids:
                count += i.duration
            r.real_duration = count

    @api.depends('songs_ids')
    def _count_songs(self):
        for r in self:
            if not r.songs_ids:
                r.number_of_songs = 0.0
            else:
                r.number_of_songs = len(r.songs_ids)
