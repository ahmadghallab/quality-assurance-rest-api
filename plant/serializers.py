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
        fields = ('id', 'month', 'year', 'unit', 'department', 'criterion', 'checked')
        model = models.Evaluation

class FilteredEvaluationSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(
            unit_id=self.context['request'].query_params.get('unit'),
            month=self.context['request'].query_params.get('month'),
            year=self.context['request'].query_params.get('year')
        )
        return super(FilteredEvaluationSerializer, self).to_representation(data)

class CustomEvaluationSerializer(serializers.ModelSerializer):
    criterion = serializers.StringRelatedField()

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related('criterion')
        return queryset

    class Meta:
        list_serializer_class = FilteredEvaluationSerializer
        fields = ('id', 'criterion', 'checked')
        model = models.Evaluation

class DepartmentEvaluationSerializer(serializers.ModelSerializer):
    department_evaluations = CustomEvaluationSerializer(many=True, read_only=True)

    @staticmethod
    def setup_eager_loading(queryset):
        # prefetch_related for "to-many" relationships
        queryset = queryset.prefetch_related('department_evaluations')
        return queryset

    class Meta:
        fields = ('id', 'name', 'department_evaluations')
        model = models.Department