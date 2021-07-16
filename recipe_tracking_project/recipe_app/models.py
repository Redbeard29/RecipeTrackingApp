from django.db import models
import re
import bcrypt
import datetime

from django.db.models.manager import EmptyManager

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['first_name']) == 0:
            errors['first_name'] = "First name is required"
        elif len(postData['first_name']) < 2 or postData['first_name'].isalpha() != True:
            errors['first_name'] = "First name must be at least 2 characters, letters only"
        if len(postData['last_name']) == 0:
            errors['last_name'] = "Last name is required"
        elif len(postData['last_name']) < 2 or postData['last_name'].isalpha() != True:
            errors['last_name'] = "Last name must be at least 2 characters, letters only"
        if len(postData['email']) == 0:
            errors['email'] = "Email is required"
        elif not email_regex.match(postData['email']):
            errors['email'] = "Invalid email address"
        existing_user = User.objects.filter(email=postData['email'])
        if len(existing_user) > 0:
            errors['email'] = "Email already in use"
        if len(postData['password']) == 0:
            errors['password'] = "Password is required"
        elif len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        elif postData['password'] != postData['confirm_password']:
            errors['password'] = "Passwords do not match"
        return errors
        
    def log_in_validator(self, postData):
        errors = {}
        existing_user = User.objects.filter(email=postData['email'])
        if len(postData['email']) == 0:
            errors['email'] = "Email is required"
        elif len(existing_user) != 1:
            errors['email'] = "User not found"
        if len(postData['password']) == 0:
            errors['password'] = "Password is required"
        if existing_user:
            if bcrypt.checkpw(postData['password'].encode(), existing_user[0].password.encode()) != True:
                errors['email'] = "Email and password do not match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class RecipeManager(models.Manager):
    def recipe_validator(self, postData):
        errors = {}
        if len(postData['title']) == 0:
            errors['title'] = 'Title is required'
        if len(postData['link_to_recipe']) == 0:
            errors['link_to_recipe'] = 'Link is required'
        elif len(postData[['link_to_recipe']]) < 6:
            errors['link_to_recipe'] = 'Link must be at least 6 characters'
        if len(postData['description']) == 0:
            errors['description'] = 'Description is required'
        current_date = datetime.date.today()
        if (postData['last_made_at']) > current_date:
            errors['last_made_at'] = 'Date cannot be in the future'

class Recipe(models.Model):
    MEAT_CHOICES = (
        ("RM", "Red Meat"),
        ("PL", "Poultry"),
        ("FI", "Fish"),
        ("VG", "Vegetarian"),
    )
    CATEGORY_CHOICES = (
        ("AM", "American"),
        ("CH", "Chinese"),
        ("EE", "Eastern European"),
        ("EN", "English"),
        ("FR", "French"),
        ("GE", "German"),
        ("GR", "Greek"),
        ("IN", "Indian"),
        ("IT", "Italian"),
        ("JP", "Japanese"),
        ("KR", "Korean"),
        ("MX", "Mexican"),
        ("OT", "Other"),
        ("SL", "Soul Food"),
    )
    title = models.CharField(max_length=90)
    picture = models.ImageField(upload_to="recipe_photo_album")
    link_to_recipe = models.URLField(max_length=200)
    description = models.TextField(blank=True)
    meat_type = models.CharField(max_length=2, choices=MEAT_CHOICES, default=MEAT_CHOICES[0][0])
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0])
    best_quantity = models.DecimalField(max_digits=3, decimal_places=2, default=1)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    comments = models.TextField(blank=True)
    last_made_at = models.DateField()
    quick_and_easy = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    have_made_before = models.BooleanField(default=False)
    saved_by = models.ForeignKey(User, related_name='saved_recipes', on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RecipeManager()
