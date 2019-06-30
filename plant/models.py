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

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Section(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, related_name='sections', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['name', 'department']

class Criterion(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, related_name='criteria', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['name', 'section']