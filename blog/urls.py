from django.urls import path
from . import views


urlpatterns = [
    path('', views.RecipeListView.as_view(), name='start'),
    path('home/', views.RecipeListView.as_view(), name='home'),
    path('about/', views.RecipeListView.as_view(), name='about'),
    path('likes/<slug:slug>/', views.RecipeLike.as_view(), name='recipe_like'),
    path('add_recipe/', views.AddRecipeFormView, name='add_recipe'),
    path('recipe_add/', views.RecipeAddView.as_view(), name='recipe-add'),
    path('add_category/', views.AddCategoryFormView, name='add-category'),
    path('recipe_mylist/', views.RecipeMyListView, name='recipe_mylist'),
    path('recipe_search', views.RecipeSearch, name='recipe-search'),
    path('recipe_update/<recipe_id>', views.RecipeUpdate, name='recipe-update'),
    path('recipe_delete/<recipe_id>', views.RecipeDelete, name='recipe_delete'),

    path('recipe/<int:pk>', views.RecipeDetailEdit.as_view(), name='recipe-edit'),
    path('<slug:slug>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
]
