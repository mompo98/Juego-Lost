import random
from odoo import models, fields, api

class survivor(models.Model):
    _name='lost.survivor'
    _description = 'SURVIVORS'

    def _generate_job(self):
        opc = random.randint(1,100)
        print("----------------------")
        print(opc)
        if (opc<80):
            job = ["Timber","Student","Police","Nursing_assistant","Shop_assistant","Mayor","Scullion"]
            return random.choice(job)

        if (opc>=80 and opc<=90):
            job = ["Worker","Teacher","Liutenant","Nurse","Supervisor","Politician","Cook"]
            return random.choice(job)

        if (opc>90):
            job = ["Architect","Engineer","Captain","Doctor","Shop_owner","President","Chef"]
            return random.choice(job)

    name = fields.Char()
    #age = fields.Integer()
    date_of_birth = fields.Date()
    mentalHealth = fields.Integer(default=50)
    hungry = fields.Integer(default=50)
    avatar = fields.Image(max_width=20, max__height=40)
    occupation =fields.Char(default=_generate_job)
    island = fields.Many2one('lost.island')

    @api.model
    def update_resources(self):
        alive_survivors = self.search([('hungry','<',100)])
        for s in alive_survivors:
            if s.mentalHealth>0:
                s.mentalHealth-=1
            if s.hungry>0:
                s.hungry-=1
            