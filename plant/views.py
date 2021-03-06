from django.db.models import Count, Sum, Q

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

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

class ListUnitEvaluation(APIView):
    def get(self, request, unit_pk, format=None):
        unit = models.Unit.objects.values(
            'name', 'management__id', 'management__name'
        ).get(
            pk=unit_pk
        )
        evaluations = models.Evaluation.objects.values(
            'month', 'year'
        ).filter(unit_id=unit_pk).distinct()

        return Response({
            'evaluations': evaluations,
            'unit': unit
        }, status=status.HTTP_200_OK)

class CreateUnitEvaluation(APIView):
    def post(self, request, unit_pk, format=None):

        month = self.request.data.get('month')
        year = self.request.data.get('year')
        
        criteria = models.Criterion.objects.all()

        evaluation_exists = models.Evaluation.objects.filter(
            month=month,
            year=year,
            unit_id=unit_pk,
            criterion_id=criteria[0].id
        )
        if evaluation_exists:
            return Response('This evaluation already done', status=status.HTTP_400_BAD_REQUEST)

        values = []
        for criterion in criteria:
            b = {'month': self.request.data.get('month'),
                'year': self.request.data.get('year'),
                'unit_id': unit_pk,
                'fulfilled': True,
                'department_id': criterion.department_id,
                'criterion_id': criterion.id
            }
            values.append(b.copy())
        
        aList = [models.Evaluation(**vals) for vals in values]
        models.Evaluation.objects.bulk_create(aList)

        return Response('Resource created', status=status.HTTP_201_CREATED)

class DeleteUnitEvaluation(APIView):
    def delete(self, request, unit_pk, format=None):
        try:
            models.Evaluation.objects.filter(
                unit_id=unit_pk,
                month=self.request.query_params.get('month'),
                year=self.request.query_params.get('year')
            ).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class DisplayUnitEvaluation(APIView):
    def get(self, request, unit_pk, format=None):
        mode = self.request.query_params.get('mode')

        if mode == 'get':
            evaluations = models.Evaluation.objects.values(
                'id','criterion__name', 'fulfilled', 'text'
            ).filter(
                unit_id=unit_pk,
                department_id=self.request.query_params.get('department'),
                month=self.request.query_params.get('month'),
                year=self.request.query_params.get('year')
            )
            return Response(evaluations, status=status.HTTP_200_OK)

        departments = models.Evaluation.objects.values(
            'department__id', 'department__name'
        ).filter(
            unit_id=unit_pk,
            month=self.request.query_params.get('month'),
            year=self.request.query_params.get('year')
        ).distinct()


        if mode == 'report':
            unit = models.Unit.objects.values(
                'name', 'management__name'
            ).get(
                pk=unit_pk
            )
            evaluations = models.Evaluation.objects.values(
                'id', 'department_id', 'criterion__name', 'fulfilled', 'text'
            ).filter(
                unit_id=unit_pk,
                month=self.request.query_params.get('month'),
                year=self.request.query_params.get('year')
            )
            return Response({
                'departments': departments,
                'evaluations': evaluations,
                'unit': unit
            }, status=status.HTTP_200_OK)

        if mode == 'edit':
            return Response(departments, status=status.HTTP_200_OK)

        return Response('missing query param (mode) available options [get, edit, report]', status=status.HTTP_400_BAD_REQUEST)

class SaveEvaluation(APIView):
    def post(self, request, format=None):
        criteria = self.request.data.get('criteria')
        fulfilled = self.request.data.get('fulfilled')
        text = self.request.data.get('text')

        if text or text == '':
            models.Evaluation.objects.filter(pk__in=criteria).update(
                text=text
            )
        else:
            models.Evaluation.objects.filter(pk__in=criteria).update(
                fulfilled=fulfilled
            )

        return Response(status=status.HTTP_200_OK)

class DisplayManagementEvaluation(APIView):
    def get(self, request, management_pk, format=None):
        evaluations = models.Evaluation.objects.values(
            'unit__name',
        ).filter(
            month=self.request.query_params.get('month'),
            year=self.request.query_params.get('year')
        ).distinct().annotate(
            total=Count('pk'),
            total_fulfilled=Count('fulfilled', filter=Q(fulfilled=True)),
            total_not_fulfilled=Count('fulfilled', filter=Q(fulfilled=False))
        )
        
        return Response(evaluations, status=status.HTTP_200_OK)