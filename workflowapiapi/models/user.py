from django.db import models

class User(models.Model):
    ADMIN = 'admin'
    CLIENT = 'client'
    WORKER = 'worker'
    
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (CLIENT, 'Client'),
        (WORKER, 'Worker'),
    ]

    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=12)
    nickname = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)