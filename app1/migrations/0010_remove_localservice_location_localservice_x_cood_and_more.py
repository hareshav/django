# Generated by Django 4.2.2 on 2023-07-13 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_remove_remoteservice_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localservice',
            name='location',
        ),
        migrations.AddField(
            model_name='localservice',
            name='x_cood',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='localservice',
            name='y_cood',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='localservice',
            name='services',
            field=models.CharField(choices=[('Chef', 'Chef'), ('Mechanic', 'Mechanic')], max_length=100),
        ),
        migrations.AlterField(
            model_name='remoteservice',
            name='services',
            field=models.CharField(choices=[('Analyst', 'Analyst'), ('ML trainer', 'ML trainer')], max_length=100),
        ),
    ]
