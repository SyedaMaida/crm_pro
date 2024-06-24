# Generated by Django 5.0.6 on 2024-06-17 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('cpassword', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=20)),
                ('industry', models.CharField(max_length=20)),
                ('noEmp', models.BigIntegerField(max_length=20)),
                ('role', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('userID', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
