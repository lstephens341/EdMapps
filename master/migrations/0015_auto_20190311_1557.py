# Generated by Django 2.0.6 on 2019-03-11 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0014_auto_20190311_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardcodesandverbiage',
            name='standardWording',
            field=models.TextField(blank=True),
        ),
    ]
