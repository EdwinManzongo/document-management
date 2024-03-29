# Generated by Django 3.2.9 on 2022-05-04 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(default=None, max_length=100)),
                ('address', models.CharField(default=None, max_length=100)),
                ('contact_number', models.IntegerField(default=None)),
                ('department', models.CharField(choices=[('', '------------'), ('information_systems', 'Information Systems'), ('computer_science', 'Computer Science'), ('business_studies_and_computing_science', 'Business Studies And Computing Science'), ('accounting', 'Accounting')], max_length=100)),
                ('student_type', models.CharField(choices=[('', '------------'), ('undergraduate', 'Undergraduate'), ('postgraduate_masters', 'Post Graduate - Masters'), ('postgraduate_doctorate', 'Post Graduate - Doctorate'), ('postgraduate_masters', 'Post Graduate - Professor')], max_length=100)),
                ('national_id_no', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('dob', models.DateField(default=None)),
                ('created_at', models.DateField(default=None)),
                ('updated_at', models.DateField(default=None)),
                ('created_by', models.IntegerField(default=None)),
            ],
        ),
    ]
