# Generated by Django 2.0.6 on 2018-12-19 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0009_auto_20181219_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='grade',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='lesson',
            name='unit',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='lesson',
            name='version',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]