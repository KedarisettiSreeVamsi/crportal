# Generated by Django 3.1.1 on 2020-11-04 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0011_event_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='disable_add',
            field=models.BooleanField(default=False),
        ),
    ]