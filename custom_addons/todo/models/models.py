# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Todo(models.Model):
    _name = 'todo.task'
    _description = 'task'

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    deadline = fields.Date('Deadline')
    is_done = fields.Boolean('Done?')
