# Generated by Django 3.1.2 on 2020-10-14 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joblist', '0004_joblist_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblist',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
