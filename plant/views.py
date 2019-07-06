import datetime

from rest_framework import generics, status
from rest_framework.response import Response

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

    def get_queryset(self):
        return self.queryset.filter(
            unit_id=self.kwargs.get('unit_pk')
        )

    def create(self, request, *args, **kwargs):
        criteria = models.Criterion.objects.all()
        for criterion in criteria:
            evaluation_exists = models.Evaluation.objects.filter(
                date=datetime.date.today().replace(day=1),
                unit_id=self.kwargs.get('unit_pk'),
                criterion_id=criterion.id
            )
            if evaluation_exists:
                return Response('This evaluation already done', status=status.HTTP_400_BAD_REQUEST)

            obj = models.Evaluation()
            obj.date = datetime.date.today().replace(day=1)
            obj.unit_id = self.kwargs.get('unit_pk')
            obj.checked = False
            obj.department_id = criterion.department_id
            obj.criterion_id = criterion.id
            obj.save()

        return Response('Resource created', status=status.HTTP_201_CREATED)
            

class RetrieveUpdateDestroyEvaluation(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Evaluation.objects.all()
    serializer_class = serializers.EvaluationSerializer