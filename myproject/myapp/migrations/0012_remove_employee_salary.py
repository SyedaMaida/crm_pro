# Generated by Django 5.0.6 on 2024-07-03 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_account_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='salary',
        ),
    ]