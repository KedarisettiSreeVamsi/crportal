# Generated by Django 3.1.1 on 2020-11-04 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_request', '0004_auto_20201104_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancerequest',
            name='image',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to='request_pics'),
        ),
    ]
