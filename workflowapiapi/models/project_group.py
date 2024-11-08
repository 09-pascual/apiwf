from django.db import models
from .group import Group
from .project import Project


class ProjectGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    # group = models.ManyToManyField("Group", through="ProjectGroup", related_name="groups")
    # project = models.ManyToManyField("Project", through="ProjectGroup", related_name="projects")