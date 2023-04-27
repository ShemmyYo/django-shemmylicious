from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views import generic, View
from django.template import RequestContext
from .models import Recipe, Category, Comment
from .forms import CommentForm, CategoryForm, AddRecipeForm, UpdateRecipeForm
from cloudinary.forms import cl_init_js_callbacks


# 404 Handler 
def handler_404(request, exception, template_name='404.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response


# 500 Handler
def handler_500(request):
    response = render(request, '500.html')
    response.status_code = 500
    return response


# 403 Handler
def handler_403(request, *args, **argv):
    response = render_to_response('403.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 403
    return response


# 400 Handler
def handler_400(request, *args, **argv):
    response = render_to_response('400.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 400
    return response


# Start View
def StartView(request):
    slider = Recipe.objects.all().order_by('?')[:12]
    return render(request, "index.html", {'slider': slider, })


# Recipe Full List Class View
class RecipestView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_date')
    template_name = 'recipe_all.html'
    paginate_by = 8


# Recipe Full List Class View - Blog (CI)
class RecipeListView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_date')
    template_name = 'recipe_list.html'
    paginate_by = 10


# Search Recipes View
def RecipeSearch(request):
    if request.method == 'POST':
        searched = str(request.POST['searched']).capitalize()
        recipes = Recipe.objects.filter(recipe_title__contains=searched)
        success_message = f"The below are your results for: { searched }!"
        return render(
            request,
            'recipe_search.html',
            {
                'searched': searched,
                'recipes': recipes
            })
    else:
        return render(request, 'recipe_search.html', {})


# Create Category View when authenticated as Superuser
def AddCategoryFormView(request):
    submitted = False
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Category successfully created!")
            return HttpResponseRedirect('/categories?submitted=True')
    else:
        form = CategoryForm
        if "submitted" is request.GET:
            submitted=True

    return render(request, "recipe_add_category.html", {'form': form, 'submitted': submitted, })


# List of Categories
class CategoryListView(generic.ListView):
    model = Category
    queryset = Category.objects.all().order_by('?')[:11]
    template_name = 'category_list.html'


# View by Category
def CategoryView(request, categories):
    find_category_name = Category.objects.get(category_name=categories)
    category_recipes = Recipe.objects.filter(category=find_category_name)
    return render(request, "recipe_list_by_category.html", {
        'categories': categories,
        'category_recipes': category_recipes,
        })


# Create My Recipe View when authenticated
def AddRecipeFormView(request):
    submitted = False
    if request.method == "POST":
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, "Recipe successfully created!")
            return HttpResponseRedirect('/recipe_add?submitted=True')
    else:
        form = AddRecipeForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "recipe_add.html", {
        'form': form,
        'submitted': submitted,
        })


# View My Recipe List View when authenticated
def RecipeMyListView(request):
    if request.user.is_authenticated:
        recipes = Recipe.objects.filter(
            author=request.user.id).order_by('-created_date')
        return render(request, 'recipe_mylist.html', {
            "recipes": recipes
        })
    else:
        return redirect('recipes')


# Update My Recipe when authenticated
def RecipeUpdate(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    form = UpdateRecipeForm(request.POST or None, instance=recipe)
    if form.is_valid():
        form.save()
        messages.success(request, "Successfully updated.")
        return redirect('recipe-mylist')
    
    return render(request, 'recipe_update.html', {
        'recipe': recipe,
        'form': form
        },)


# Delete My Recipe when authenticated
def RecipeDelete(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    recipe.delete()
    messages.warning(request, "Recipe deleted!")
    return redirect('recipe-mylist')


# Delete Comment when Superuser
def CommentDelete(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    messages.warning(request, "Comment deleted!")
    return redirect('recipes')


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
            comment_form.instance.post_author = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe_name = recipe
            comment.save()
            messages.success(
                request, "Successfully posted.Your comment is awaiting Admin's approval.")
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


# Recipe Blog View Class (CI)
class RecipeBlogView(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(active=True).order_by('created_date')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "recipe_blog.html",
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
            comment_form.instance.post_user= request.user
            comment_form.instance.post_author = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe_name = recipe
            comment.save()
            messages.success(
                request, 
                "Successfully posted. Comment is awaiting Admin's approval"
                )
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_blog.html",
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
            messages.warning(request, "Oh no! I'm sorry you don't like it.")       
        else:
            post.likes.add(request.user)
            messages.success(request, "Thank you! I appriciate your opinion!")
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
