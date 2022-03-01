from django.db import models

# Create your models here.

class EmailSubscriber(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField()