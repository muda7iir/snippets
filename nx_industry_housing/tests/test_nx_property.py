from odoo.tests.common import TransactionCase


class TestNxProperty(TransactionCase):

    def test_property_creation(self):
        prop = self.env['nx.property'].create({
            'name': 'Test Villa',
            'status': 'available',
            'booking_status': 'booked',
            'payment_status': 'partial',
            'price': 5000000,
            'website_published': True,
        })
        self.assertEqual(prop.name, 'Test Villa')
        self.assertTrue(prop.website_url)
