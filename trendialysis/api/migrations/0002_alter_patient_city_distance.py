# Generated by Django 4.0.4 on 2022-04-25 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='city_distance',
            field=models.FloatField(default=32000),
        ),
    ]