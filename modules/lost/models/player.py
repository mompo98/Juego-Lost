import random
from odoo import models, fields, api

class player(models.Model):
    _name = 'lost.player'
    _description = 'PLAYERS'

    name = fields.Char()
    island = fields.One2many('lost.island','player')

    

