# Generated by Django 3.1.4 on 2020-12-14 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uab', '0002_auto_20201214_2301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urls',
            old_name='urls_text',
            new_name='url_name',
        ),
    ]