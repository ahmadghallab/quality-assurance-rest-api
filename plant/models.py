from django.db import models

class Management(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Unit(models.Model):
    name = models.CharField(max_length=100)
    management = models.ForeignKey(Management, related_name='units', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['name', 'management']