from django.db import models
from .group import Group
from .worker import Worker

class GroupWorker(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
