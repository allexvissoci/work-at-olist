from rest_framework import serializers
from bill.models import Bill


class BillSerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()
    started_date = serializers.SerializerMethodField()
    started_time = serializers.SerializerMethodField()
    destination = serializers.SerializerMethodField()

    class Meta:
        model = Bill
        fields = ["destination",
                  "started_date",
                  "started_time",
                  "duration",
                  "call_price"]

    def get_call_id(self, obj):
        return obj.call_start_record.call_id

    def get_destination(self, obj):
        return obj.call_start_record.destination

    def get_started_date(self, obj):
        return obj.call_start_record.timestamp.date()

    def get_started_time(self, obj):
        return obj.call_end_record.timestamp.time()

    def get_duration(self, obj):
        return obj.call_duration
