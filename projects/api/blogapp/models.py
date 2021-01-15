from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=112)
    email = models.EmailField()
    message = models.TextField()