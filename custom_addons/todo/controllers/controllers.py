# -*- coding: utf-8 -*-
# from odoo import http


# class ./customAddons/todo(http.Controller):
#     @http.route('/./custom_addons/todo/./custom_addons/todo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./custom_addons/todo/./custom_addons/todo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('./custom_addons/todo.listing', {
#             'root': '/./custom_addons/todo/./custom_addons/todo',
#             'objects': http.request.env['./custom_addons/todo../custom_addons/todo'].search([]),
#         })

#     @http.route('/./custom_addons/todo/./custom_addons/todo/objects/<model("./custom_addons/todo../custom_addons/todo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./custom_addons/todo.object', {
#             'object': obj
#         })
