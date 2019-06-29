from rest_framework import serializers

from . import models

class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = models.Management

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'management')
        model = models.Unit