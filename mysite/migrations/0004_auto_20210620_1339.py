# Generated by Django 3.2.3 on 2021-06-20 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_rename_whether_trafficaccident_weather'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speedmeasuring',
            name='ViolationType',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='speedmeasuring',
            name='cameraType',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='speedmeasuring',
            name='direction',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='speedmeasuring',
            name='dist',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='speedmeasuring',
            name='limit',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='speedmeasuring',
            name='location',
            field=models.CharField(max_length=40),
        ),
    ]
