# Generated by Django 3.0.5 on 2020-06-02 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20200602_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='def.jpg', null=True, upload_to='image_pics'),
        ),
    ]