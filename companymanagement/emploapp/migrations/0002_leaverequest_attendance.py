# Generated by Django 4.1 on 2024-09-10 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emploapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('reason', models.TextField()),
                ('approved', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emploapp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('clock_in_time', models.DateTimeField(auto_now_add=True)),
                ('clock_out_time', models.DateTimeField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emploapp.profile')),
            ],
        ),
    ]
