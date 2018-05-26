from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from bill.models import Bill
from record.models import Record
from datetime import datetime
import pytz


class CalculationTestCase(APITestCase):
    def setUp(self):
        self.start_url = '/startrecord/'
        self.end_url = '/endrecord/'
        self.client = APIClient()

    def test_call_price_before_initial_reference_charge_time(self):
        # "
        # start record timestamp < initial reference charge time and
        # end record timestamp < initial reference charge time
        # "
        start_record = Record.objects.create(
            type='start',
            timestamp=datetime(2018, 5, 22, 1, 00, 00, tzinfo=pytz.UTC),
            call_id='1',
            source='41999814484',
            destination='41999814483'
        )

        Record.objects.create(
            type='end',
            call_id='1',
            timestamp=datetime(2018, 5, 22, 5, 00, 00, tzinfo=pytz.UTC),
        )

        bill = Bill.objects.get(call_start_record__pk=start_record.pk)
        self.assertEqual(float(bill.call_price), 0.36)

    def test_call_price_after_end_reference_charge_time(self):
        # "
        # start record timestamp > end reference charge time and
        # end record timestamp > end reference charge time
        # "
        start_record = Record.objects.create(
            type='start',
            timestamp=datetime(2018, 5, 22, 22, 30, 00, tzinfo=pytz.UTC),
            call_id='2',
            source='41999814484',
            destination='41999814483'
        )

        Record.objects.create(
            type='end',
            call_id='2',
            timestamp=datetime(2018, 5, 22, 23, 30, 00, tzinfo=pytz.UTC),
        )

        bill = Bill.objects.get(call_start_record__pk=start_record.pk)
        self.assertEqual(float(bill.call_price), 0.36)

    def test_call_price_with_call_charge_one(self):
        # "
        # start record timestamp < reference charge time and
        # end record timestamp >= initial reference charge time
        # and end record timestamp <= end reference charge time
        # "
        start_record = Record.objects.create(
            type='start',
            timestamp=datetime(2018, 5, 22, 2, 00, 00, tzinfo=pytz.UTC),
            call_id='3',
            source='41999814484',
            destination='41999814483'
        )

        Record.objects.create(
            type='end',
            call_id='3',
            timestamp=datetime(2018, 5, 22, 8, 00, 00, tzinfo=pytz.UTC),
        )

        bill = Bill.objects.get(call_start_record__pk=start_record.pk)
        self.assertEqual(float(bill.call_price), 11.16)

    def test_call_price_with_call_charge_two(self):
        # "
        # start record timestamp >= initial reference charge time and
        # start record timestamp <= end reference charge time and
        # end record timestamp > end reference charge time
        # "
        start_record = Record.objects.create(
            type='start',
            timestamp=datetime(2018, 5, 22, 19, 00, 00, tzinfo=pytz.UTC),
            call_id='4',
            source='41999814484',
            destination='41999814483'
        )

        Record.objects.create(
            type='end',
            call_id='4',
            timestamp=datetime(2018, 5, 22, 23, 00, 00, tzinfo=pytz.UTC),
        )

        bill = Bill.objects.get(call_start_record__pk=start_record.pk)
        self.assertEqual(float(bill.call_price), 16.56)

    def test_call_price_with_call_charge_three(self):
        # "
        # start record timestamp < initial reference charge time and
        # end record timestamp > end reference charge time
        # "
        start_record = Record.objects.create(
            type='start',
            timestamp=datetime(2018, 5, 22, 2, 00, 00, tzinfo=pytz.UTC),
            call_id='5',
            source='41999814484',
            destination='41999814483'
        )

        Record.objects.create(
            type='end',
            call_id='5',
            timestamp=datetime(2018, 5, 22, 23, 00, 00, tzinfo=pytz.UTC),
        )

        bill = Bill.objects.get(call_start_record__pk=start_record.pk)
        self.assertEqual(float(bill.call_price), 86.76)
