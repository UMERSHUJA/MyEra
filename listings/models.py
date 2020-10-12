from django.db import models
from datetime import datetime



class Startup(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False)

    prices = models.CharField(max_length=200)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    is_sponsered = models.BooleanField(default=False)
    submission_date = models.DateTimeField(default=datetime.now, blank=False)
    def __str__(self):
        return self.product_name




class JobList(models.Model):
    job_title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False)

    experience = models.CharField(max_length=200)
    job_type = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    job_link = models.BooleanField(default=False)
    submission_date = models.DateTimeField(default=datetime.now, blank=False)
    def __str__(self):
        return self.job_title

