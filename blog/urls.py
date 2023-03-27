from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeLike, AddRecipeFormView, RecipeAddView, AddCategoryFormView, RecipeMyListView, RecipeDetailEdit


urlpatterns = [
    path('', RecipeListView.as_view(), name='start'),
    path('home/', RecipeListView.as_view(), name='home'),
    path('about/', RecipeListView.as_view(), name='about'),
    path('likes/<slug:slug>/', RecipeLike.as_view(), name='recipe_like'),
    path('add_recipe/', AddRecipeFormView, name='add_recipe'),
    path('recipe_add/', RecipeAddView.as_view(), name='recipe-add'),
    path('add_category', AddCategoryFormView, name='add-category'),
    path('recipe_mylist', RecipeMyListView, name='recipe_mylist'),
    path('recipe/<int:pk>', RecipeDetailEdit.as_view(), name='recipe-edit'),
    path('<slug:slug>/', RecipeDetailView.as_view(), name='recipe_detail'),
]
