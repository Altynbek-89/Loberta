# Generated by Django 3.1.4 on 2020-12-14 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uab', '0003_auto_20201214_2321'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='urls',
            options={'verbose_name': 'URL'},
        ),
        migrations.RemoveField(
            model_name='urls',
            name='status',
        ),
        migrations.AlterField(
            model_name='urls',
            name='url_name',
            field=models.URLField(verbose_name='URL name'),
        ),
    ]
