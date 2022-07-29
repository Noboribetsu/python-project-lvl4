from django.urls import reverse
from django.test import TestCase


class AppTest(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('index_page'))
        self.assertEqual(response.status_code, 200)
