# Generated by Django 4.0.1 on 2022-01-18 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MetricsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dockermetrics',
            name='container_id',
            field=models.CharField(max_length=50),
        ),
    ]