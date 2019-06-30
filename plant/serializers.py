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
        fields = ('id', 'name', 'section')
        model = models.Criterion

class SectionSerializer(serializers.ModelSerializer):
    criteria = CriterionSerializer(many=True, read_only=True)

    class Meta:
        fields = ('id', 'name', 'department', 'criteria')
        model = models.Section

class DepartmentSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        fields = ('id', 'name', 'sections')
        model = models.Department