# Generated by Django 2.2.4 on 2019-09-08 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PNM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('onyen', models.CharField(max_length=20, unique=True, verbose_name='Onyen')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('open_one', models.BooleanField(verbose_name='Open Recruitment One')),
                ('open_two', models.BooleanField(verbose_name='Open Recruitment Two')),
                ('open_three', models.BooleanField(verbose_name='Open Recruitment Three')),
                ('open_friday', models.BooleanField(verbose_name='Open Recruitment Friday')),
                ('closed_one', models.BooleanField(verbose_name='Closed Recruitment One')),
                ('closed_two', models.BooleanField(verbose_name='Closed Recruitment Two')),
                ('closed_three', models.BooleanField(verbose_name='Closed Recruitment Three')),
                ('potluck', models.BooleanField(verbose_name='Potluck')),
            ],
        ),
    ]
