# Generated by Django 3.0.6 on 2020-06-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaryApp', '0002_auto_20200623_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='src',
            field=models.ImageField(upload_to='media/image'),
        ),
    ]
