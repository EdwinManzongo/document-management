# Generated by Django 3.2.9 on 2022-05-04 20:44

import cabinet.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dapartment', models.CharField(blank=True, choices=[('', '------------'), ('information_systems', 'Information Systems'), ('computer_science', 'Computer Science'), ('business_studies_and_computing_science', 'Business Studies And Computing Science'), ('accounting', 'Accounting')], default='no', max_length=100)),
                ('cabinet', models.CharField(max_length=100)),
                ('document_type', models.CharField(blank=True, choices=[('', '------------'), ('undergraduate_dissertation', 'Undergraduate Dissertation'), ('masters_thesis', 'Masters Thesis'), ('phd_thesis', 'PHD Thesis'), ('research', 'Research')], default='no', max_length=100)),
                ('document_title', models.CharField(default='', max_length=30)),
                ('date', models.DateField()),
                ('document', models.FileField(upload_to=cabinet.models.Cabinet.create_unique_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'jpg', 'png', 'jpeg', 'doc', 'xlsx'])])),
                ('notes', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('created_at', models.DateField(default=None)),
                ('updated_at', models.DateField(default=None)),
                ('created_by', models.IntegerField(default=None)),
            ],
        ),
    ]
