# Generated by Django 4.2.5 on 2023-09-26 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_evento_usuarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data_criacao',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
