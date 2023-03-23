from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeLike, AddRecipeFormView, AddCategoryFormView


urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
    path('<slug:slug>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('likes/<slug:slug>', RecipeLike.as_view(), name='recipe_like'),
    path('add_recipe', AddRecipeFormView, name='add-recipe'),
    path('add_category', AddCategoryFormView, name='add-category'),
]
