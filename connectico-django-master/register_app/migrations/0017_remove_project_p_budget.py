# Generated by Django 2.2.1 on 2020-03-10 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register_app', '0016_user_org_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='p_budget',
        ),
    ]
