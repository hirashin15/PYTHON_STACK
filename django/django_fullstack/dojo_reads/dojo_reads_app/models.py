from django.db import models
import re
# Create your models here.

class UserManager(models.Manager):
  def reg_Validator(self, post_data):
    errors = {}
    if len(post_data["name"]) < 2:
      errors["name"] = "Name must contain more than 2 characters"
    email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not email_regex.match(post_data["email"]):
      errors["email"] = "Invalid email address"
    if len(post_data["password"]) < 2:
      errors["password"] = "Password must be at least 2 characters"
    if post_data["password"] != post_data["confirm_password"]:
      errors["confirm_password"] = "Passwords do not match"
    return errors
  
  def login_validator(self, post_data):
    errors = {}
    email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not email_regex.match(post_data['email']):
      errors['email'] = "Invalid email address!"
    if len(post_data['password']) < 2:
      errors['password'] = "Password must be at least 2 characters."
    return errors

  def review_validator(self, post_data):
    errors={}
    if len(post_data["title"]) == 0:
      errors["title"] = "Must include a title to submit review."
    if len(post_data["rating"]) == 0:
      errors["rating"] = "Must include a rating to submit review."
    return errors


class User(models.Model):
  name = models.CharField(max_length = 50)
  alias = models.CharField(max_length=10)
  email = models.EmailField()
  password = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()
  # reviews_by_user = list of reviews made by user

class Author(models.Model):
  name = models.CharField(max_length = 50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  # books = list of books written by author

class BookManager(models.Model):
  def book_validator(self, post_data):
    errors={}
    if len(post_data["title"]) == 0:
      errors["title"] = "Must include a title to submit review."
    if len(post_data["rating"]) == 0:
      errors["rating"] = "Must include a rating to submit review."
    return errors


class Book(models.Model):
  title = models.CharField(max_length = 25)
  authors = models.ManyToManyField(Author, related_name="books")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = BookManager()
  # reviews_for_book = list of reviews for this book

class ReviewManager(models.Model):
  def review_validator(self, post_data):
    errors={}
    if len(post_data["review"]) == 0:
      errors["review"] = "Must include a review to submit review."
    if len(post_data["rating"]) == 0:
      errors["rating"] = "Must include a rating to submit review."
    return errors

class Review(models.Model):
  text = models.TextField()
  rating = models.IntegerField(default = 1)
  review_by = models.ForeignKey(User, related_name="reviews_by_user", on_delete=models.CASCADE)
  review_for = models.ForeignKey(Book, related_name="reviews_for_book", on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = ReviewManager()
