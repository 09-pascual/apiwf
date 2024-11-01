from django.db import models 
from .worker import Worker
from .project import Project

class ProjectWorker(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
