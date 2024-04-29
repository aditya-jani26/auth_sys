# Generated by Django 5.0.4 on 2024-04-29 08:46

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0017_alter_customtoken_created_at_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customtoken',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 8, 46, 50, 60606)),
        ),
        migrations.AlterField(
            model_name='leave',
            name='leaveEndDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='leaveStartDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
