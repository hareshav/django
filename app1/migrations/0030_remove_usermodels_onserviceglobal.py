# Generated by Django 4.2.2 on 2023-08-11 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_alter_usermodels_onserviceglobal_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodels',
            name='onserviceglobal',
        ),
    ]
