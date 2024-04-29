# Generated by Django 5.0.4 on 2024-04-29 07:07

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0011_alter_customtoken_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customtoken',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 7, 7, 40, 434034)),
        ),
        migrations.AlterField(
            model_name='project',
            name='assignToProject_Manager',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='assign_to_pm', to='department.customuser'),
            preserve_default=False,
        ),
    ]
