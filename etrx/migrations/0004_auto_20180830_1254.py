# Generated by Django 2.1 on 2018-08-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etrx', '0003_laptops_ram'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptops',
            name='screen_size',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='laptops',
            name='storage',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='laptops',
            name='weight',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
