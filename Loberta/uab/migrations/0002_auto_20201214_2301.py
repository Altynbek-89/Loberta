# Generated by Django 3.1.4 on 2020-12-14 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='status',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='urls',
            name='urls_text',
            field=models.URLField(),
        ),
    ]
