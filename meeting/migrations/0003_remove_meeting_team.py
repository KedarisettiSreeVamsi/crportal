# Generated by Django 3.1.1 on 2020-11-10 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0002_auto_20201110_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='team',
        ),
    ]
