# Generated by Django 2.2.1 on 2020-03-06 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_app', '0015_inviteduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='org_creator',
            field=models.BooleanField(null=True, verbose_name='Creator'),
        ),
    ]
