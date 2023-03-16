from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import ListView
from .models import Recipe


class RecipeListView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_date')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(active=True).order_by('created_date')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "recipe_detail.html",
            {
                "post": recipe,
                "comments": comments,
                "liked": liked,

            }
        )
