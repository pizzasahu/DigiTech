# Generated by Django 2.1 on 2018-08-30 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etrx', '0005_laptops_lap_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptops',
            name='lap_id',
            field=models.IntegerField(null=True),
        ),
    ]
