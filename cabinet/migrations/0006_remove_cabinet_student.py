# Generated by Django 3.2.9 on 2022-05-24 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0005_remove_cabinet_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cabinet',
            name='student',
        ),
    ]
