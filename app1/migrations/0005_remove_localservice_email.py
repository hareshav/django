# Generated by Django 4.2.2 on 2023-07-12 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_localservice_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localservice',
            name='email',
        ),
    ]
