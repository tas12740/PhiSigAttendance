# Generated by Django 3.0.3 on 2020-02-15 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipanel', '0005_auto_20190920_1604'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('vote_onyen', 'pnm_number')},
        ),
    ]