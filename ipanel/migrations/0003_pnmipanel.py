# Generated by Django 2.2.5 on 2019-09-20 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipanel', '0002_auto_20190913_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='PNMIPanel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('L', 'Locked'), ('O', 'Open')], max_length=10)),
            ],
        ),
    ]