from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from rest_framework import generics
from .serializers import UserSerializer, RecipeSerializer
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def recipe_list(request):
    if 'user_id' in request.session:
        current_user = User.objects.get(id=request.session['user_id'])
        current_users_recipes = Recipe.objects.filter(saved_by=current_user)
        recipe_list = current_users_recipes.filter(have_made_before=True)
        favorited_recipes = current_users_recipes.filter(is_favorite=True)
        saved_recipes = current_users_recipes.filter(have_made_before=False)
        context = {
            'user': current_user,
            'all_recipes': recipe_list,
            'favorite_recipes' : favorited_recipes,
            'saved_recipes' : saved_recipes,
        }
        return render(request, 'recipe_list.html', context)
    else:
        return redirect('/login')

def registration_display(request):
    return render(request, 'registration.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/register_page')
        hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hashed_password
        )
        request.session['user_id'] = new_user.id
        return redirect('/my_recipe_list')
    return redirect('/register_page')

def login_display(request):
    return render(request, 'login.html')

def login(request):
    if request.method == "POST":
        errors = User.objects.log_in_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login')
        this_user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = this_user.id
        return redirect('/my_recipe_list')
    
    return redirect('/login')

def add_recipe_display(request):
    return render(request, 'add_recipe.html')

def add_recipe(request):
    if request.method == "POST":
        errors = Recipe.objects.recipe_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/add_recipe')       
    return redirect('/my_recipe_list')

class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RecipeView(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RecipeListView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer