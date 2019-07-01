from rest_framework import generics

from . import models
from . import serializers

class ListCreateManagement(generics.ListCreateAPIView):
    queryset = models.Management.objects.all()
    serializer_class = serializers.ManagementSerializer

class RetrieveUpdateDestroyManagement(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Management.objects.all()
    serializer_class = serializers.ManagementSerializer

class ListCreateUnit(generics.ListCreateAPIView):
    queryset = models.Unit.objects.all()
    serializer_class = serializers.UnitSerializer

class RetrieveUpdateDestroyUnit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Unit.objects.all()
    serializer_class = serializers.UnitSerializer

class ListCreateDepartment(generics.ListCreateAPIView):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer

class RetrieveUpdateDestroyDepartment(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer

class ListCreateCriterion(generics.ListCreateAPIView):
    queryset = models.Criterion.objects.all()
    serializer_class = serializers.CriterionSerializer

class RetrieveUpdateDestroyCriterion(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Criterion.objects.all()
    serializer_class = serializers.CriterionSerializer

class ListCreateEvaluation(generics.ListCreateAPIView):
    queryset = models.Evaluation.objects.all()
    serializer_class = serializers.EvaluationSerializer