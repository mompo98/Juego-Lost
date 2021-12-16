# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api

class event(models.Model):
    _name = 'negocity.event'
    _description = 'Events'

    name = fields.Char()
    player = fields.Many2many('lost.player')
    event = fields.Reference([('lost.building','Building'),('lost.player','Player'),('lost.survivor','Survivor')])
    description = fields.Text()