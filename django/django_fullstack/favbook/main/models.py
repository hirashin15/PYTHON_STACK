from django.db import models
import re

class UserManager(models.Manager):
    def Uservalidator(self, post_data):
        errors = {}
        if len(post_data["fname"]) < 2:
            errors['fname'] = "First Name must contain more than 2 character."
        if len(post_data['lname']) < 2:
            errors['lname'] = "Last Name must contain more than 2 character."
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(post_data['email']):
            errors['email'] = "Invalid email address!"
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be at least 8 characters."
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password'] = "Passwords do not match."
        return errors

    def loginvalidator(self, post_data):
        errors= {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(post_data['email']):
            errors['email'] = "Invalid email address!"
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be at least 8 characters."
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    # uploads = list of books uploaded by a given user
    # userfavs = list of books users like

class BookManager(models.Manager):
    def Bookvalidator(self, post_data):
        errors = {}
        if len(post_data["title"]) < 1:
            errors['title'] = "Title must be at least 1 character long."
            
        if len(post_data["desc"]) < 5:
            errors['desc'] = "Description must be at least 5 character long."
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    upload = models.ForeignKey(User, related_name = "uploads", on_delete = models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name = "userfavs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()


