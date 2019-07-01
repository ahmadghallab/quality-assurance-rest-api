from rest_framework import serializers

from . import models

class UnitSerializer(serializers.ModelSerializer):
    # management_id = serializers.StringRelatedField()
    
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

class DepartmentSerializer(serializers.ModelSerializer):
    # criteria = CriterionSerializer(many=True, read_only=True)
    # evaluation_departments = EvaluationSerializer(many=True, read_only=True)

    class Meta:
        fields = ('id', 'name')
        model = models.Department