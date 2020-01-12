# Generated by Django 2.2.4 on 2019-09-08 20:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0005_auto_20190825_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='unique_id',
            field=models.CharField(max_length=4, unique=True, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Event Code'),
        ),
    ]
