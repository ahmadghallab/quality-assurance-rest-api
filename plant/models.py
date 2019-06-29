from django.db import models

class Management(models.Model):
    name = models.CharField(max_length=100, unique=True)
