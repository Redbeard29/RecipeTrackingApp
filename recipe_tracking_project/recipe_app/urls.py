from django.urls import path
from . import views

urlpatterns = [
    path('user', views.UserView.as_view()),
    path('recipe', views.RecipeView.as_view()),
    path('user/list', views.UserListView.as_view()),
    path('recipe/list', views.RecipeListView.as_view())
]

