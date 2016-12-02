from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Job(models.Model):
    job_title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    job_area = models.CharField(max_length=12)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    pub_date = models.DateTimeField('date job published')

    def __str__(self):
        return self.job_title


class candidate(models.Model):
    job_applied  = models.ForeignKey(Job, on_delete=models.CASCADE)
    name         = models.CharField(max_length=50)
    cv           = models.CharField(max_length=100)
    nationality  = models.CharField(max_length=10)
    date_applied = models.DateField('Applied')

    def __str__(self):
        return self.name