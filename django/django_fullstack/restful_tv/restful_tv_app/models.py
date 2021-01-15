from django.db import models
from datetime import datetime, date

class TVshowManager(models.Manager):
    def basic_validator(self, data):
        errors = {}
        if len(data["title"]) < 2:
            errors["title"] = "Title should be at least 2 characters"
        print(datetime.strptime(data["date"], "%Y-%m-%d").date())
        print("*"*100)
        if datetime.strptime(data["date"], "%Y-%m-%d").date() > date.today():
            "Cannot set date to future date"
        if len(data["desc"]) > 0 & len(data["desc"]) < 10:
            errors["desc"] = "TV show description should be at least 10 characters"
        return errors

class TVshow(models.Model):
    title = models.CharField(max_length=255)
    release = models.DateField()
    desc = models.TextField(default = "No Description!")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TVshowManager()
    
class Network(models.Model):
    name = models.CharField(max_length=255)
    shows = models.ManyToManyField(TVshow, related_name = "networks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)