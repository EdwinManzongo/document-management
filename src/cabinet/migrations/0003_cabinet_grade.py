# Generated by Django 3.2.9 on 2022-07-20 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0002_auto_20220609_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabinet',
            name='grade',
            field=models.CharField(default='', max_length=30),
        ),
    ]
