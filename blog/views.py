from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, reverse
from django.contrib import messages
from django.views.generic import ListView
from .models import Recipe
from .forms import CommentForm, CategoryForm
from .forms import AddRecipeForm


def AddRecipeFormView(request):
    submitted = False
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_recipe?submitted=True')
    else:
        form = AddRecipeForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "add_recipe.html", {'form': form, 'submitted': submitted, })


def AddCategoryFormView(request):
    form = CategoryForm

    return render(request, "add_category.html", {'form': form})



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
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()

            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(active=True).order_by('created_date')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = recipe
            messages.success(request, "Successfully posted. Your comment is awaiting Admin's approval.")
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "post": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()

            },
        )


class RecipeLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Recipe, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
