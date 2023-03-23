from .models import Comment, Recipe, Category
from django import forms
from django.forms import ModelForm



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name', 'featured_image',)


# Create a Recipe Form
class AddRecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('recipe_title', 'category', 'featured_image',
        'featured_comment', 'recipe_ingridients',
        'recipe_instructions', 'excerpt', 'author',)
