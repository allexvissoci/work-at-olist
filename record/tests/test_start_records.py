from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class RecordTestCase(APITestCase):
    def setUp(self):
        self.start_url = '/startrecord/'
        self.client = APIClient()

    def test_create_start_record_without_timestamp(self):
        params = {
            'type': 'start',
            'timestamp': '',
            'call_id': '1',
            'source': '41999814484',
            'destination': '41999814483'
        }

        response = self.client.post(self.start_url, params)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0}.'
                         .format(response.status_code))

    def test_create_start_record_without_call_id(self):
        params = {
            'type': 'start',
            'timestamp': '2018-05-25T05:00',
            'call_id': '',
            'source': '41999814484',
            'destination': '41999814483'
        }

        response = self.client.post(self.start_url, params)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0}.'
                         .format(response.status_code))

    def test_create_start_record_with_less_than_ten_character(self):
        params = {
            'type': 'start',
            'timestamp': '2018-05-25T05:00',
            'call_id': '1',
            'source': '419998144',
            'destination': '41999814483'
        }

        response = self.client.post(self.start_url, params)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0}.'
                         .format(response.status_code))

    def test_create_start_record_with_more_than_eleven_character(self):
        params = {
            'type': 'start',
            'timestamp': '2018-05-25T05:00',
            'call_id': '1',
            'source': '419998144844',
            'destination': '41999814483'
        }

        response = self.client.post(self.start_url, params)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0}.'
                         .format(response.status_code))

    def test_create_destination_record_with_less_than_ten_character(self):
        params = {
            'type': 'start',
            'timestamp': '2018-05-25T05:00',
            'call_id': '1',
            'source': '41999814484',
            'destination': '419998144'
        }

        response = self.client.post(self.start_url, params)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0}.'
                         .format(response.status_code))

    def test_create_destination_record_with_more_than_eleven_character(self):
        params = {
            'type': 'start',
            'timestamp': '2018-05-25T05:00',
            'call_id': '1',
            'source': '41999814483',
            'destination': '419998144844'
        }

        response = self.client.post(self.start_url, params)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0}.'
                         .format(response.status_code))

    def test_create_a_valid_start_record(self):
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

    def test_create_two_start_record_with_duplicate_call_id(self):
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
            'type': 'start',
            'timestamp': '2018-05-25T05:00',
            'call_id': '1',
            'source': '41999814484',
            'destination': '41999814483'
        }

        response = self.client.post(self.start_url, params)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0}.'
                         .format(response.status_code))

    def test_create_a_start_record_with_same_source_and_destination(self):
        params = {
            'type': 'start',
            'timestamp': '2018-05-25T05:00',
            'call_id': '1',
            'source': '41999814484',
            'destination': '41999814484'
        }

        response = self.client.post(self.start_url, params)
        self.assertEqual(response.status_code, 400,
                         'Expected Response Code 400, received {0}.'
                         .format(response.status_code))
