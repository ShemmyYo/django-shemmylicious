from django.urls import path
from . import views


urlpatterns = [
    path('', views.StartView, name='start'),
    path('home/', views.RecipeListView.as_view(), name='home'),
    path('recipes/', views.RecipestView.as_view(), name='recipes'),
    path('likes/<slug:slug>/', views.RecipeLike.as_view(), name='recipe_like'),
    
    path('recipe_category_add/', views.AddCategoryFormView, name='add-category'),
    path('recipe_add/', views.AddRecipeFormView, name='add-recipe'),
    path('recipe_mylist/', views.RecipeMyListView, name='recipe-mylist'),
    path('recipe_search/', views.RecipeSearch, name='recipe-search'),
    path('recipe_update/<recipe_id>/', views.RecipeUpdate, name='recipe-update'),
    path('recipe_delete/<recipe_id>/', views.RecipeDelete, name='recipe-delete'),

    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('category/<str:categories>/', views.CategoryView, name='category'),

    path('recipe/<slug:slug>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
]
