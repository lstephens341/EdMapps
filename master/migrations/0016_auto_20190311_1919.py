# Generated by Django 2.0.6 on 2019-03-11 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0015_auto_20190311_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='standardcodesandverbiage',
            old_name='version',
            new_name='standardVersion',
        ),
    ]