from django.db import models
from .user import User
from .project import Project

class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    availability_status = models.CharField(max_length=50)
    projects = models.ManyToManyField(Project, through='ProjectWorker')
