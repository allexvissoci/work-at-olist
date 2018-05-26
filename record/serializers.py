from rest_framework import serializers
from record.models import Record


class StartRecordSerializer(serializers.ModelSerializer):

    type = serializers.CharField(default="start", initial="start",
                                 read_only=True)

    class Meta:
        model = Record
        fields = (
            'id',
            'type',
            'call_id',
            'timestamp',
            'source',
            'destination'
        )

    def validate(self, data):
        if data['source'] == data['destination']:
            message = "Source and destination can't be the same"
            raise serializers.ValidationError(message)
        else:
            data['type'] = 'start'
            return data


class EndRecordSerializer(serializers.ModelSerializer):

    type = serializers.CharField(default="end", initial="end", read_only=True)

    class Meta:
        model = Record
        fields = (
            'id',
            'type',
            'call_id',
            'timestamp',
        )

    def validate(self, data):
        if Record.objects.filter(call_id=data['call_id']).exists():
            start_record = Record.objects.get(call_id=data['call_id'])
            if(start_record.timestamp < data['timestamp']):
                data['type'] = 'end'
                return data
            else:
                message = "Initial record time greater than end record time."
                raise serializers.ValidationError(message)
        else:
            message = "No initial record."
            raise serializers.ValidationError(message)
