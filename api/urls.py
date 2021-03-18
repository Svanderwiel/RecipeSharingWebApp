from django.urls import path
from .views import RecipeView

urlpatterns = [
    path('home', RecipeView.as_view()),
]