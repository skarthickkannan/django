# Generated by Django 3.0.5 on 2020-06-01 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='comment',
        ),
    ]
