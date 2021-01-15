from django.db import models
import re

class UserManager(models.Manager):
    def validator(self, post_data):
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
    
        
    def login_validator(self, post_data):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(post_data['email']):
            errors['email'] = "Invalid email address!"
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be at least 8 characters."
        return errors

class User(models.Model):
    fname = models.CharField(max_length=23)
    lname = models.CharField(max_length=23)
    email = models.EmailField(max_length=255)
    hashpw = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    message = models.CharField(max_length=255)
    message_by = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment_by = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE)
    comment_for = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

