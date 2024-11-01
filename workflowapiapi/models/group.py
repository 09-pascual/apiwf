from django.db import models
from .worker import Worker
from .project import Project

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    workers = models.ManyToManyField(Worker, through='GroupWorker')
    projects = models.ManyToManyField(Project, through='ProjectGroup')
