# Generated by Django 4.2.2 on 2023-08-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_remove_usermodels_globalservicefrom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodels',
            name='globalServiceFrom',
            field=models.TimeField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='usermodels',
            name='globalServiceTo',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
    ]
