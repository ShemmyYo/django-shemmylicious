from .models import Comment, Recipe, Category
from django import forms
from django.forms import ModelForm
from cloudinary.models import CloudinaryField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name', 'featured_image',)


# Create a Recipe Form
class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'recipe_title',
            'slug',
            'category',
            'featured_image',
            'featured_comment',
            'recipe_ingridients',
            'recipe_instructions',
            'excerpt',
            'author',
            )

        labels = {
            'recipe_title': '',
            'slug': '',
            'category': '',
            'featured_image': '',
            'featured_comment': '',
            'recipe_ingridients': '',
            'recipe_instructions': '',
            'excerpt': '',
            'author': '',
        }
        widgets = {
            'recipe_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recipe Title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'slug'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            #'featured_image': forms.URLInput(attrs={'class': 'form-control', 'type': 'file'}),
            'featured_comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Featured Comment'}),
            'recipe_ingridients': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingridients'}),
            'recipe_instructions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Instructions'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional Info'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Author'}),
        }
