# Generated by Django 4.2.19 on 2025-02-10 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logemenent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('localisation', models.CharField(max_length=200)),
                ('lien', models.URLField()),
                ('prix', models.IntegerField()),
                ('place', models.IntegerField()),
                ('loges', models.ManyToManyField(blank=True, related_name='loge', to='gestion.invite')),
            ],
        ),
        migrations.AddField(
            model_name='invite',
            name='logement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dors', to='gestion.logemenent'),
        ),
    ]
