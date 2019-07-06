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

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'date', 'unit', 'department', 'criterion', 'checked')
        model = models.Evaluation
    
    def create(self, validated_data):
        return models.Evaluation.objects.create(**validated_data)

class DepartmentSerializer(serializers.ModelSerializer):
    criteria = CriterionSerializer(many=True, read_only=True)
    
    class Meta:
        fields = ('id', 'name', 'criteria')
        model = models.Department