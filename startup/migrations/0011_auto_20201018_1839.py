# Generated by Django 3.1.2 on 2020-10-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0010_auto_20201017_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='image',
            field=models.ImageField(upload_to='Startup'),
        ),
    ]
