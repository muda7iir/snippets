# -*- coding: utf-8 -*-
from odoo import api, fields, models
import re


def _slug(value):
    """Generate a URL-friendly slug from a record or string."""
    try:
        # If it's a record, use display_name
        text = value.display_name if hasattr(value, 'display_name') else str(value)
        record_id = value.id if hasattr(value, 'id') else ''
    except:
        text = str(value)
        record_id = ''
    
    # Convert to lowercase and remove special characters
    slug_text = re.sub(r'[^a-zA-Z0-9\s-]', '', text).lower()
    slug_text = re.sub(r'\s+', '-', slug_text).strip('-')
    
    # Add ID if available
    if record_id:
        return f"{slug_text}-{record_id}" if slug_text else str(record_id)
    return slug_text or 'page'


class NxProperty(models.Model):
    _name = 'nx.property'
    _description = 'NX Property'
    _inherit = ['website.published.mixin', 'mail.thread']
    _order = 'sequence, id desc'

    name = fields.Char(required=True, translate=True, tracking=True)
    sequence = fields.Integer(default=10)
    website_published = fields.Boolean(default=True, tracking=True)
    type_id = fields.Many2one('nx.property.type', tracking=True)
    partner_id = fields.Many2one('res.partner', string='Customer', tracking=True)
    status = fields.Selection([
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('sold', 'Sold'),
    ], default='available', tracking=True)
    booking_status = fields.Selection([
        ('draft', 'Draft'),
        ('booked', 'Booked'),
        ('purchased', 'Purchased'),
    ], default='draft', tracking=True)
    payment_status = fields.Selection([
        ('unpaid', 'Unpaid'),
        ('partial', 'Partially Paid'),
        ('paid', 'Paid'),
    ], default='unpaid', tracking=True)
    price = fields.Monetary()
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)
    area = fields.Float(string='Area (sq ft)')
    bedrooms = fields.Integer()
    bathrooms = fields.Integer()
    location = fields.Char()
    description = fields.Html()
    image_ids = fields.One2many('nx.property.image', 'property_id')
    website_url = fields.Char(compute='_compute_website_url')

    @api.depends('name')
    def _compute_website_url(self):
        for record in self:
            record.website_url = '/properties/%s' % _slug(record)
