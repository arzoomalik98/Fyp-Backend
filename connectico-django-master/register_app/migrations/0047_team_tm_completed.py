# Generated by Django 2.2.1 on 2020-07-09 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_app', '0046_project_p_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='tm_completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
