# Generated by Django 4.2.19 on 2025-02-19 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_rename_quantité_extras_quantite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
            ],
        ),
    ]
