"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_ipxe(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/boot/')
        self.assertTrue(response.content.split()[0] == '#!ipxe')
        
        response = self.client.get('/boot/aa:bb:cc:dd:ee:ff')
        self.assertTrue(response.content.split()[0] == '#!ipxe')
