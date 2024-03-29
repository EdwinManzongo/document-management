# Generated by Django 3.2.9 on 2022-02-22 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authenticate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=None, max_length=100)),
                ('firstname', models.CharField(default=None, max_length=100)),
                ('lastname', models.CharField(default=None, max_length=100)),
                ('access_level', models.CharField(blank=True, choices=[('', '------------'), ('Admin', 'Admin'), ('Supervisor', 'Supervisor'), ('Team Leader', 'Team Leader'), ('Agent', 'Agent'), ('Client', 'Client')], default=None, max_length=100, null=True)),
            ],
        ),
    ]
