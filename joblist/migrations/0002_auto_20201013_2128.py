# Generated by Django 3.1.2 on 2020-10-13 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joblist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblist',
            name='company_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='joblist',
            name='icon',
            field=models.ImageField(upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='joblist',
            name='job_link',
            field=models.CharField(max_length=100),
        ),
    ]
