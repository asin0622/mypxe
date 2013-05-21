"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from boot.models import Host


class SimpleTest(TestCase):
    
    def test_memtest_function(self):
        host = Host()
        host.mac = 'aa:bb:cc:dd:ee:ff'
        host.save()
        
        response = self.client.get('/memtest/start/aa:bb:cc:dd:ee:ff')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/memtest/good/aa:bb:cc:dd:ee:ff')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/memtest/bad/aa:bb:cc:dd:ee:ff')
        self.assertEqual(response.status_code, 200)