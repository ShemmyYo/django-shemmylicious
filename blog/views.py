from django.shortcuts import render, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView

from .models import Recipe
from .forms import CommentForm, CategoryForm, AddRecipeForm
from .forms import AddRecipeForm

# Start View
def StartView(request):
    return render(request, "index.html", {})


# About View
def AboutView(request):
    return render(request, "about.html", {})


# Search Recipes View
def RecipeSearch(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        recipes = Recipe.objects.filter(recipe_title__contains=searched)
        return render(request,
        'recipe_search.html',
        {'searched': searched,
        'recipes': recipes})
    else:
        return render(request, 'recipe_search.html', {})


# Recipe Full List Class View (CI)
class RecipeListView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_date')
    template_name = 'recipe_list.html'
    paginate_by = 10


# Create Category View when authenticated as Admin?!!!!!!!!!!!!!!!!!!!
def AddCategoryFormView(request):
    form = CategoryForm

    return render(request, "add_category.html", {'form': form})


# Create My Recipe View when authenticated
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




# Create My Recipe View when authenticated _ TBD
class RecipeAddView(generic.CreateView):
    model = Recipe
    template_name = 'recipe_add.html'
    fields = '__all__'









# View My Recipe List View when authenticated
def RecipeMyListView(request):
    if request.user.is_authenticated:
        recipes = Recipe.objects.filter(author=request.user.id).order_by('-created_date')
        return render (request, 'recipe_mylist.html', {
            "recipes": recipes
        })
    else:
        messages.success(request, ("Success!"))
        return redirect('home')


# Update My Recipe when authenticated
def RecipeUpdate(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    form = AddRecipeForm(request.POST or None, instance=recipe)
    if form.is_valid():
        form.save()
        messages.success(request, "Successfully updated.")
        return redirect('recipe_mylist')
    
    return render(request, 'recipe_update.html',
        {'recipe': recipe,
        'form': form},)


# Delete My Recipe when authenticated
def RecipeDelete(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    recipe.delete()
    return redirect('recipe_mylist')




# CI WALKTHROUGH BELOW


# Recipe Details View Class (CI)
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


# Recipe Likes View Class (CI)
class RecipeLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Recipe, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
