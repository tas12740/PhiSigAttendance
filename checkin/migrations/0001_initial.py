# Generated by Django 2.2.4 on 2019-08-20 17:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Sibling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('onyen', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('house', models.CharField(blank=True, choices=[('Rollawood', 'Rollawood'), ('Torchia', 'Torchia'), ('Harryhill', 'Harryhill'), ('', '')], max_length=10, null=True)),
                ('status', models.CharField(blank=True, choices=[('Active', 'Active')], max_length=20, null=True)),
                ('big', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='checkin.Sibling')),
                ('big_alumni', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='checkin.Alumni')),
            ],
        ),
        migrations.CreateModel(
            name='GPATracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)])),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('sibling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkin.Sibling', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('unique_id', models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(4)])),
                ('description', models.CharField(blank=True, max_length=100)),
                ('date_time', models.DateTimeField()),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkin.EventType')),
            ],
        ),
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkin.Event')),
                ('sibling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkin.Sibling')),
            ],
        ),
    ]
