from __future__ import unicode_literals

from django.db import models


# Create your models here.
class SavedJob(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    jobId = models.IntegerField(default=0)
    title = models.CharField(default='',max_length=200)
    city = models.CharField(default='', max_length=50)
    state = models.CharField(default='',max_length=50)
    company = models.CharField(default='',max_length=200)
    salary = models.CharField(default='',max_length=50)
    salaryPer = models.CharField(default='',max_length=50)
    description = models.CharField(default='',max_length=200)
    sponsored = models.BooleanField(default=False,max_length=50)
    expired = models.BooleanField(default=False,max_length=50)
    expireInDays = models.IntegerField(default=0)
    postedDaysAgo = models.IntegerField(default=0)

    def __str__(self):
        return self.title
