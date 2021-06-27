from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from rest_framework import generics
from .serializers import UserSerializer, RecipeSerializer

# Create your views here.
def index(request):
    user_list = User.objects.all()
    recipe_list = Recipe.objects.all()
    context = {
        'recipes': recipe_list,
        'users': user_list,
    }
    return render(request, 'index.html', context)


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