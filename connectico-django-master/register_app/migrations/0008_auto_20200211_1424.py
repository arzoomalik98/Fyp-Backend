# Generated by Django 2.2.1 on 2020-02-11 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_app', '0007_auto_20191203_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='photo_address',
            field=models.TextField(blank=True, null=True, verbose_name='Photo address'),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='photo_address',
            field=models.TextField(blank=True, null=True, verbose_name='Photo address'),
        ),
    ]