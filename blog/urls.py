from django.urls import path
from .views import RecipeListView
from .views import RecipeDetailView


urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
    path('<slug:slug>/', RecipeDetailView.as_view(), name='recipe_detail'),
]
