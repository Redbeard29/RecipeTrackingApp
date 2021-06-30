from django.urls import path
from . import views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('my_recipe_list', views.recipe_list),
    path('register', views.registration_display),
    path('register_attempt', views.register),
    path('login', views.login_display),
    path('login_attempt', views.login),
    path('user', views.UserView.as_view()),
    path('recipe', views.RecipeView.as_view()),
    path('user/list', views.UserListView.as_view()),
    path('recipe/list', views.RecipeListView.as_view())
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

