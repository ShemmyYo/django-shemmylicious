from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeLike, AddRecipeFormView, AddCategoryFormView, RecipeMyListView


urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
    path('recipe_mylist', RecipeMyListView.as_view(), name='recipe_mylist'),
    path('<slug:slug>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('likes/<slug:slug>', RecipeLike.as_view(), name='recipe_like'),
    path('add_recipe', AddRecipeFormView, name='add-recipe'),
    path('add_category', AddCategoryFormView, name='add-category'),
]
