# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 15:16
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=20, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')])),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=10)),
                ('email_id', models.EmailField(max_length=40)),
                ('apply_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('exp_required', models.IntegerField(default=0)),
                ('salary', models.IntegerField(default=500000, error_messages={'salary': 'Only Digits allowed'})),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=20, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')])),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6)),
                ('contact', models.CharField(max_length=10)),
                ('email_id', models.EmailField(max_length=40)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='jobs',
            name='recruiter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_post', to='restapp.Recruiter'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='apply_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_to_job', to='restapp.Jobs'),
        ),
    ]
