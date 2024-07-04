# Generated by Django 5.0.6 on 2024-07-03 16:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_remove_employee_company_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='company_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.company'),
        ),
    ]
