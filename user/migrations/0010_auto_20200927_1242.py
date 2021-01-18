# Generated by Django 3.1.1 on 2020-09-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_profile_is_cr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cgpa',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='profile',
            name='section',
            field=models.CharField(choices=[('B01', 'B01'), ('B02', 'B02'), ('B03', 'B03'), ('B04', 'B04'), ('B05', 'B05'), ('B06', 'B06'), ('B07', 'B07'), ('B08', 'B08'), ('B09', 'B09'), ('B10', 'B10'), ('B11', 'B11'), ('B12', 'B12'), ('B13', 'B13'), ('B14', 'B14'), ('B15', 'B15'), ('B16', 'B16'), ('B17', 'B17'), ('B18', 'B18'), ('B19', 'B19')], max_length=4),
        ),
    ]