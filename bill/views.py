from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from bill.serializers import BillSerializer
from bill.models import Bill
from datetime import datetime


class BillView(viewsets.ViewSet):

    def list(self, request):
        subscriber = request.GET.get('subscriber', None)
        reference = request.GET.get('reference', None)

        if subscriber is None:
            message = 'Please enter a subscriber'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        queryset = Bill.objects.filter(call_start_record__source=subscriber)
        if reference is not None:
            try:
                d = datetime.strptime(reference, '%m/%Y')
                data = {'call_end_record__timestamp__year': d.year,
                        'call_end_record__timestamp__month': d.month}

            except ValueError as e:
                message = 'Please enter a valid date fomat %m/%Y'
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            now = datetime.now()
            month = now.month - 1
            data = {'call_end_record__timestamp__year': now.year,
                    'call_end_record__timestamp__month': month}

        queryset = queryset.filter(**data)
        ctx = {'request': request}
        serializer = BillSerializer(queryset, context=ctx, many=True)
        return Response(serializer.data)
