# Generated by Django 2.1.15 on 2020-05-23 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basefunction', '0003_userip_create_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userip',
            options={'ordering': ['-create_time']},
        ),
    ]
