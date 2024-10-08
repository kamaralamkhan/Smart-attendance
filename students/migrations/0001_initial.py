# Generated by Django 4.1.11 on 2023-12-03 16:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('enrollment_number', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=50)),
                ('session', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=15)),
                ('parents_phone_number', models.CharField(max_length=15)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('created_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('updated_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('A', 'Absent'), ('P', 'Present')], max_length=1)),
                ('teacher_id', models.CharField(blank=True, max_length=150, null=True)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('created_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('updated_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('student', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='attendance_records', to='students.student')),
            ],
        ),
    ]
