# Generated by Django 4.2.2 on 2023-07-04 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('services', models.CharField(choices=[('samayal', 'samayal'), ('carpenter', 'carpenter'), ('plumber', 'plumber'), ('Astronaut', 'Astronaut'), ('security', 'security')], max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
