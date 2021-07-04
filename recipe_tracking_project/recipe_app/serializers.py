from rest_framework import serializers
from .models import User, Recipe

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'created_at', 'updated_at')

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'picture', 'link_to_recipe', 'description', 'meat_type', 'category', 
        'best_quantity', 'rating', 'comments', 'last_made_at', 'quick_and_easy', 'is_favorite', 'have_made_before', 'saved_by', 'created_at', 'updated_at')