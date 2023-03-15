from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from .models import Recipe


class RecipeListView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_date')
    template_name = 'index.html'
    paginate_by = 6
