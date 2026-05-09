# -*- coding: utf-8 -*-
from odoo import fields, models


class NxPropertyImage(models.Model):
    _name = 'nx.property.image'
    _description = 'NX Property Image'
    _order = 'sequence, id'

    name = fields.Char(required=True)
    sequence = fields.Integer(default=10)
    property_id = fields.Many2one('nx.property', required=True, ondelete='cascade')
    image_1920 = fields.Image(required=True)
