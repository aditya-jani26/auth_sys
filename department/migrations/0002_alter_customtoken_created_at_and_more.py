# Generated by Django 5.0.4 on 2024-04-25 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customtoken',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 25, 12, 35, 17, 230797)),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectStartDate',
            field=models.DateField(),
        ),
    ]
