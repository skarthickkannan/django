# Generated by Django 3.0.5 on 2020-06-02 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_reply_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reply',
        ),
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='main.Comment'),
        ),
    ]
