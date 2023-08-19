# Generated by Django 4.2.2 on 2023-08-09 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_alter_localservice_id_alter_remoteservice_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodels',
            name='location',
        ),
        migrations.AddField(
            model_name='usermodels',
            name='globalServiceFrom',
            field=models.TimeField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='usermodels',
            name='globalServiceTo',
            field=models.TimeField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='usermodels',
            name='localServiceFrom',
            field=models.TimeField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='usermodels',
            name='localServiceTo',
            field=models.TimeField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='usermodels',
            name='x_cood',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='usermodels',
            name='y_cood',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='usermodels',
            name='onserviceglobal',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_hire_remote', to='app1.remoteservice'),
        ),
        migrations.AlterField(
            model_name='usermodels',
            name='onservicelocal',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_hire_local', to='app1.localservice'),
        ),
    ]
