# Generated by Django 2.2.1 on 2020-06-04 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register_app', '0026_auto_20200427_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_lead_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_lead', to=settings.AUTH_USER_MODEL),
        ),
    ]
