# Generated by Django 4.2.2 on 2023-08-09 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_remove_usermodels_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodels',
            name='globalServiceFrom',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='usermodels',
            name='globalServiceTo',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='usermodels',
            name='localServiceFrom',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='usermodels',
            name='localServiceTo',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
    ]