# Generated by Django 3.2.9 on 2022-06-09 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisors', '0002_remove_supervisor_supervisor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='supervisor',
            name='supervisor_id',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
