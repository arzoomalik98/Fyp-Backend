# Generated by Django 2.2.1 on 2020-06-20 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_app', '0040_auto_20200620_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='t_status',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
