# Generated by Django 4.2.2 on 2023-07-12 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_remove_localservice_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='localservice',
            name='email',
            field=models.EmailField(default='haresh', max_length=254, unique=True),
        ),
    ]
