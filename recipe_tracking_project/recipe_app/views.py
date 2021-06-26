from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import random
import bcrypt
import time

# Create your views here.
def index(request):
    user_recipes = Recipe.objects.all()
    context = {
        'recipes': user_recipes,
    }
    return render(request, "index.html", context)
