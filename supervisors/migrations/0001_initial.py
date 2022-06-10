# Generated by Django 3.2.9 on 2022-06-07 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supervisor_id', models.CharField(default=None, max_length=100)),
                ('fullname', models.CharField(default=None, max_length=100)),
                ('address', models.CharField(default=None, max_length=100)),
                ('contact_number', models.CharField(default=None, max_length=100)),
                ('department', models.CharField(choices=[('', '------------'), ('information_systems', 'Information Systems'), ('computer_science', 'Computer Science'), ('business_studies_and_computing_science', 'Business Studies And Computing Science'), ('accounting', 'Accounting')], max_length=100)),
                ('created_at', models.DateField(default=None)),
                ('updated_at', models.DateField(default=None)),
                ('created_by', models.CharField(default=None, max_length=100)),
            ],
        ),
    ]
