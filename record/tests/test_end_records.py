from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class RecordTestCase(APITestCase):
    def setUp(self):
        self.start_url = '/startrecord/'
        self.end_url = '/endrecord/'
        self.client = APIClient()

    def test_create_end_record_without_call_id(self):
        params = {
            'type': 'end',
            'call_id': '',
            'timestamp': '2018-05-25T05:00',
        }

        response = self.client.post(self.end_url, params)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0}.'
                         .format(response.status_code))

    def test_create_end_record_with_invalid_call_id(self):
        params = {
            'type': 'end',
            'call_id': '65655654',
            'timestamp': '2018-05-25T05:00',
        }

        response = self.client.post(self.end_url, params)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0}.'
                         .format(response.status_code))

    def test_create_end_record_without_timestamp(self):
        params = {
            'type': 'end',
            'call_id': '1',
            'timestamp': '',
        }

        response = self.client.post(self.end_url, params)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0}.'
                         .format(response.status_code))

    def test_create_a_valid_end_record(self):
        params = {
            'type': 'start',
            'timestamp': '2018-05-25T05:00',
            'call_id': '1',
            'source': '41999814484',
            'destination': '41999814483'
        }

        response = self.client.post(self.start_url, params)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0}.'
                         .format(response.status_code))

        params = {
            'type': 'end',
            'call_id': '1',
            'timestamp': '2018-05-25T10:00',
        }

        response = self.client.post(self.end_url, params)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0}.'
                         .format(response.status_code))

    def test_create_end_record_timestamp_lt_than_start_record_timestamp(self):
        params = {
            'type': 'start',
            'timestamp': '2018-05-25T05:00',
            'call_id': '2',
            'source': '41999814484',
            'destination': '41999814483'
        }

        response = self.client.post(self.start_url, params)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0}.'
                         .format(response.status_code))

        params = {
            'type': 'end',
            'call_id': '2',
            'timestamp': '2018-05-25T03:00',
        }

        response = self.client.post(self.end_url, params)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0}.'
                         .format(response.status_code))
