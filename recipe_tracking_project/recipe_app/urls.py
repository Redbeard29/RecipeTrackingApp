from django.urls import path
from . import views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('user', views.UserView.as_view()),
    path('recipe', views.RecipeView.as_view()),
    path('user/list', views.UserListView.as_view()),
    path('recipe/list', views.RecipeListView.as_view())
]

