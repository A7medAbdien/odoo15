# -*- coding: utf-8 -*-
# from odoo import http


# class OmInheritance(http.Controller):
#     @http.route('/om_inheritance/om_inheritance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_inheritance/om_inheritance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_inheritance.listing', {
#             'root': '/om_inheritance/om_inheritance',
#             'objects': http.request.env['om_inheritance.om_inheritance'].search([]),
#         })

#     @http.route('/om_inheritance/om_inheritance/objects/<model("om_inheritance.om_inheritance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_inheritance.object', {
#             'object': obj
#         })
