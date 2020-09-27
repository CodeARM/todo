from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
import datetime

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    where = models.CharField(max_length=25, default="where")
    when = models.DateField(max_length=11, default="01/01/2035")
    project = models.CharField(max_length=50, default="inbox")
    area = models.CharField(max_length=75, default="aof is?")

    def __str__(self):
        return self.title

class Area(models.Model):
    aof = models.CharField(max_length=75, default="none")
    describe = models.CharField(max_length=500, default="none")

    def __str__(self):
        return self.aof

class Project(models.Model):
    project = models.CharField(max_length=75, default="none")
    define = models.CharField(max_length=500, default="none")

    def __str__(self):
        return self.project