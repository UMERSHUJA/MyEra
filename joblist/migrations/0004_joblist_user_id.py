# Generated by Django 3.1.2 on 2020-10-14 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joblist', '0003_joblist_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblist',
            name='user_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]