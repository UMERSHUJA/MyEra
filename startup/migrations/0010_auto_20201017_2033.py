# Generated by Django 3.1.2 on 2020-10-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0009_auto_20201017_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='image',
            field=models.ImageField(upload_to='photos/%Y/%m/%d'),
        ),
    ]