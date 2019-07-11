from django.db import models

class Management(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=100)
    management = models.ForeignKey(Management, related_name='units', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['name', 'management']

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Criterion(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, related_name='criteria', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['name', 'department']

    def __str__(self):
        return self.name

class Evaluation(models.Model):
    month = models.SmallIntegerField()
    year = models.SmallIntegerField()
    unit = models.ForeignKey(Unit, related_name='unit_evaluations', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='department_evaluations', on_delete=models.CASCADE)
    criterion = models.ForeignKey(Criterion, related_name='criterion_evaluations', on_delete=models.CASCADE)
    checked = models.BooleanField()
