# Generated by Django 3.2.1 on 2021-11-09 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_employee_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.TextField(default=None),
        ),
    ]
