# Generated by Django 3.0.5 on 2020-06-01 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='Unknown', max_length=80),
        ),
    ]
