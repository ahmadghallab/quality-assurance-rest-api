# Generated by Django 2.2.2 on 2019-07-22 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0014_remove_criterion_suggested_solution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='checked',
        ),
        migrations.AddField(
            model_name='evaluation',
            name='fulfilled',
            field=models.NullBooleanField(),
        ),
    ]