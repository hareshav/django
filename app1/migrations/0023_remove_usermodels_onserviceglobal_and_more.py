# Generated by Django 4.2.2 on 2023-08-09 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_remove_usermodels_globalserviceto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodels',
            name='onserviceglobal',
        ),
        migrations.RemoveField(
            model_name='usermodels',
            name='onservicelocal',
        ),
        migrations.AddField(
            model_name='usermodels',
            name='onserviceglobal',
            field=models.ManyToManyField(blank=True, null=True, related_name='current_hire_remote', to='app1.remoteservice'),
        ),
        migrations.AddField(
            model_name='usermodels',
            name='onservicelocal',
            field=models.ManyToManyField(blank=True, null=True, related_name='current_hire_local', to='app1.localservice'),
        ),
    ]
