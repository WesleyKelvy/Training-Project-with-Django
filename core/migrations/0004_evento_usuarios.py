# Generated by Django 4.2.5 on 2023-09-26 03:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_rename_data_criaco_evento_data_criacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='usuarios',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
