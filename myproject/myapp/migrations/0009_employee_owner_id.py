# Generated by Django 5.0.6 on 2024-06-30 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_account_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='owner_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.owner'),
        ),
    ]
