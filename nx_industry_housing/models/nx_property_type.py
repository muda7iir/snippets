# -*- coding: utf-8 -*-
from odoo import fields, models


class NxPropertyType(models.Model):
    _name = 'nx.property.type'
    _description = 'NX Property Type'
    _order = 'sequence, id'

    name = fields.Char(required=True, translate=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
