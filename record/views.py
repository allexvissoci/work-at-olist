from record.serializers import StartRecordSerializer, EndRecordSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import viewsets


class StartRecordView(mixins.CreateModelMixin, viewsets.GenericViewSet):

    serializer_class = StartRecordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class EndRecordView(mixins.CreateModelMixin, viewsets.GenericViewSet):

    serializer_class = EndRecordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)
