import random
from odoo import models, fields, api


class island(models.Model):
    _name='lost.island'
    _description = 'ISLAND'

    name = fields.Char()
    gold = fields.Integer()
    productivity = fields.Integer(compute= '_get_productivity')
    security = fields.Integer(compute= '_get_security')
    supply = fields.Integer(compute= '_get_supply')
    survivors = fields.One2many('lost.survivor','island')
    buildings = fields.One2many('lost.building','island')

    @api.depends('buildings')
    def _get_security(self):
        for c in self:
            total = 0
            for s in c.buildings:
                if s.security and self:
                    total =total + s.security
            print(total)
            c.security = total

    @api.depends('buildings')
    def _get_productivity(self):
        for c in self:
            total = 0
            for s in c.buildings:
                if s.productivity and self:
                    total =total + s.productivity
            print(total)
            c.productivity = total

    @api.depends('buildings')
    def _get_supply(self):
        for c in self:
            total = 0
            for s in c.buildings:
                if s.supply and self:
                    total =total + s.supply
            print(total)
            c.supply = total

    @api.depends('island')
    def generate_gold(self):
        self.gold+=100

    @api.depends('island')
    def empty_gold(self):
        self.gold=0
        
    player = fields.Many2one('lost.player')