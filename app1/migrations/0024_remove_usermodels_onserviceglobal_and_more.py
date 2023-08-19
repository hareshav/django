# Generated by Django 4.2.2 on 2023-08-11 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0023_remove_usermodels_onserviceglobal_and_more'),
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
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_hire_remote', to='app1.remoteservice'),
        ),
        migrations.AddField(
            model_name='usermodels',
            name='onservicelocal',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_hire_local', to='app1.localservice'),
        ),
    ]
