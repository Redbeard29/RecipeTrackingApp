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
        recipe_list = Recipe.objects.filter(saved_by=current_user)
        context = {
            'user': current_user,
            'recipes': recipe_list,
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