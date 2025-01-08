# Generated by Django 5.1.3 on 2024-12-24 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecturer_id', models.CharField(max_length=20, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('class_code', models.CharField(max_length=10)),
                ('time_spent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=20, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('class_code', models.CharField(max_length=10)),
                ('time_spent', models.IntegerField()),
            ],
        ),
    ]
