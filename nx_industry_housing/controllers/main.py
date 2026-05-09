# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class NxHousingController(http.Controller):

    @http.route(['/properties'], type='http', auth='public', website=True)
    def properties_listing(self, **kwargs):
        properties = request.env['nx.property'].sudo().search([
            ('website_published', '=', True),
        ], order='sequence, id desc')
        values = {
            'properties': properties,
            'page_name': 'nx_properties_listing',
        }
        return request.render('nx_industry_housing.nx_properties_listing', values)

    @http.route(['/properties/<model("nx.property"):property_record>'], type='http', auth='public', website=True)
    def property_detail(self, property_record, **kwargs):
        if not property_record.website_published:
            return request.not_found()
        values = {
            'property_record': property_record,
            'page_name': 'nx_property_detail',
        }
        return request.render('nx_industry_housing.nx_property_detail', values)

    @http.route(['/portal/properties'], type='http', auth='user', website=True)
    def portal_properties(self, **kwargs):
        partner = request.env.user.partner_id
        properties = request.env['nx.property'].sudo().search([
            ('partner_id', '=', partner.id),
        ], order='id desc')
        values = {
            'partner': partner,
            'properties': properties,
            'page_name': 'nx_portal_properties',
        }
        return request.render('nx_industry_housing.nx_portal_properties', values)
