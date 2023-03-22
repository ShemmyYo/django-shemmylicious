from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeLike


urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
    path('<slug:slug>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('likes/<slug:slug>', RecipeLike.as_view(), name='recipe_like'),
]
