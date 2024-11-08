from django.db import models
from .client import Client

class Project(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('upcoming', 'Upcoming'),
    ]
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    expected_duration = models.IntegerField()
    groups = models.ManyToManyField("Group", through="ProjectGroup", related_name="groups")
