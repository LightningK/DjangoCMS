# Generated by Django 2.1.15 on 2020-05-29 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0002_auto_20200523_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='show_name',
            field=models.CharField(default=1024, max_length=10),
            preserve_default=False,
        ),
    ]
