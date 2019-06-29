from rest_framework import generics

from . import models
from . import serializers

class ListCreateManagement(generics.ListCreateAPIView):
    queryset = models.Management.objects.all()
    serializer_class = serializers.ManagementSerializer

class RetrieveUpdateDestroyManagement(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Management.objects.all()
    serializer_class = serializers.UnitSerializer

class ListCreateUnit(generics.ListCreateAPIView):
    queryset = models.Unit.objects.all()
    serializer_class = serializers.UnitSerializer

class RetrieveUpdateDestroyUnit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Unit.objects.all()
    serializer_class = serializers.UnitSerializer