# Generated by Django 4.2.2 on 2023-08-11 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0030_remove_usermodels_onserviceglobal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodels',
            name='onservicelocal',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.localservice'),
        ),
    ]
