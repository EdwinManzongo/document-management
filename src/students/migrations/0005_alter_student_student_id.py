# Generated by Django 3.2.9 on 2022-05-26 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_student_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
