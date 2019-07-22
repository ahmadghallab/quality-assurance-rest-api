from rest_framework import serializers

from . import models

class UnitSerializer(serializers.ModelSerializer):    
    class Meta:
        fields = ('id', 'name', 'management')
        model = models.Unit

class ManagementSerializer(serializers.ModelSerializer):
    units = UnitSerializer(many=True, read_only=True)
    class Meta:
        fields = ('id', 'name', 'units')
        model = models.Management

class CriterionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'department')
        model = models.Criterion

class DepartmentSerializer(serializers.ModelSerializer):
    criteria = CriterionSerializer(many=True, read_only=True)
    
    class Meta:
        fields = ('id', 'name', 'criteria')
        model = models.Department

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'month', 'year', 'unit', 'department', 'criterion', 'fulfilled', 'text')
        model = models.Evaluation