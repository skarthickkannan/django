# Generated by Django 3.0.5 on 2020-06-02 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_post_dislikes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='image_pics'),
        ),
    ]
