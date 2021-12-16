import random
from odoo import models, fields, api

class building(models.Model):
    _name='lost.building'
    _description='BUILDING'

    name = fields.Char()
    productivity = fields.Integer()
    security = fields.Integer()
    supply = fields.Integer()
    island = fields.Many2one('lost.island')
