# Generated by Django 2.2.5 on 2019-09-19 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0007_auto_20190919_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sibling',
            name='house',
            field=models.CharField(blank=True, choices=[('Rollawood', 'Rollawood'), ('Torchia', 'Torchia'), ('Harryhill', 'Harryhill'), ('Bigelow', 'Bigelow'), ('No House', 'No House')], max_length=10, null=True, verbose_name='House'),
        ),
        migrations.AlterField(
            model_name='sibling',
            name='pronouns',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Pronouns'),
        ),
    ]