# -*- coding: utf-8 -*-
# from odoo import http


# class Provaquatre(http.Controller):
#     @http.route('/provaquatre/provaquatre/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/provaquatre/provaquatre/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('provaquatre.listing', {
#             'root': '/provaquatre/provaquatre',
#             'objects': http.request.env['provaquatre.provaquatre'].search([]),
#         })

#     @http.route('/provaquatre/provaquatre/objects/<model("provaquatre.provaquatre"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('provaquatre.object', {
#             'object': obj
#         })
