# Generated by Django 3.2.9 on 2021-11-13 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('BSIT (Bachelor of Science in Information Technology)', 'BSIT (Bachelor of Science in Information Technology)'), ('BIT (Bachelor in Industrial Technology)', 'BIT (Bachelor in Industrial Technology)')], max_length=100, null=True)),
                ('bsit_grad', models.BooleanField(default=False)),
                ('bit_grad', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('Employed', 'Employed'), ('Unemployed', 'Unemployed')], max_length=100, null=True)),
                ('employed', models.BooleanField(default=False)),
                ('unemployed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('profile_pic', models.ImageField(blank=True, default='default_profile_2.png', null=True, upload_to='')),
                ('firstname', models.CharField(max_length=200, null=True)),
                ('middlename', models.CharField(max_length=200, null=True)),
                ('lastname', models.CharField(max_length=200, null=True)),
                ('bdate', models.DateField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('contactnum', models.CharField(max_length=200, null=True)),
                ('year_graduated', models.CharField(max_length=200, null=True)),
                ('password_holder', models.CharField(blank=True, max_length=50, null=True)),
                ('bsit_grad', models.BooleanField(default=False)),
                ('bit_grad', models.BooleanField(default=False)),
                ('employedGrad', models.BooleanField(default=False)),
                ('unemployedGrad', models.BooleanField(default=False)),
                ('graduates', models.BooleanField(default=False)),
                ('adminApprover', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('course_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracer.coursetype')),
                ('employmentstat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracer.employmentstatus')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
