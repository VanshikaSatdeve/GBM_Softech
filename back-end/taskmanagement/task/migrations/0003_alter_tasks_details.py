# Generated by Django 3.2.19 on 2024-08-04 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_tasks_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='details',
            field=models.CharField(max_length=1000),
        ),
    ]
