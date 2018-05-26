from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class BillTestCase(APITestCase):
    def setUp(self):
        self.bill_url = '/bill/'
        self.client = APIClient()

    def test_list_bill_without_subscriber(self):
        response = self.client.get(self.bill_url)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0}.'
                         .format(response.status_code))

    def test_list_bill_with_subscriber_without_reference(self):
        url = self.bill_url+"?subscriber=41999814484"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0}.'
                         .format(response.status_code))

    def test_list_bill_with_subscriber_with_reference(self):
        url = self.bill_url+"?subscriber=41999814484&reference=05/2018"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0}.'
                         .format(response.status_code))

    def test_list_bill_with_invalid_reference(self):
        url = self.bill_url+"?subscriber=41999814484&reference=2018/02"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0}.'
                         .format(response.status_code))
