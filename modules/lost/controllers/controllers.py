# -*- coding: utf-8 -*-
# from odoo import http


# class Lost(http.Controller):
#     @http.route('/lost/lost/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lost/lost/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lost.listing', {
#             'root': '/lost/lost',
#             'objects': http.request.env['lost.lost'].search([]),
#         })

#     @http.route('/lost/lost/objects/<model("lost.lost"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lost.object', {
#             'object': obj
#         })
