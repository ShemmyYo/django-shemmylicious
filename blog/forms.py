from django import forms
from django.forms import ModelForm
from .models import Comment, Recipe, Category
from cloudinary.models import CloudinaryField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


# Create a Comment Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_title', 'comment_body',)


# Create a Category Form
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name', 'featured_comment', 'featured_image', )

        widgets = {
            'category_name': forms.TextInput(attrs={
                'class': 'form-control, mb-3',
                'placeholder': 'Type in Category Name'
                }),
            'featured_comment': forms.TextInput(attrs={
                'class': 'form-control, mb-3',
                'placeholder': 'Type in Category Comment'
                }),
            'featured_image': forms.FileInput(attrs={
                'class': "form-control, mb-3",
                'type': "file"
                }),
        }

# Create a Recipe Form
class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'recipe_title',
            'category',
            'featured_comment',
            'recipe_ingridients',
            'recipe_instructions',
            'excerpt',
            'featured_image',
        )

        widgets = {
            'recipe_title': forms.TextInput(attrs={
                'class': 'form-control, mb-3',
                'placeholder': 'Type in Recipe Title'
                }),
            'category': forms.Select(attrs={
                'class': 'form-select-lg, mb-3'
                }),
            'featured_comment': forms.TextInput(attrs={
                'class': 'form-control, mb-3'
                }),
            'recipe_ingridients': SummernoteWidget(attrs={
                'summernote': {
                    'width': '100%',
                    'height': '300px',
                    'placeholder': 'Type in ingridients here...'
                    }
                }),
            'recipe_instructions': SummernoteWidget(attrs={
                'summernote': {
                    'width': '100%',
                    'height': '300px',
                    'placeholder': 'Provide instructions here...'
                    }
                }),
            'excerpt': forms.TextInput(attrs={
                'class': 'form-control, mb-3',
                'placeholder': 'Additional info info (e.g. nutrition facts etc.) as required go here...'
                }),
            'author': forms.Select(attrs={'class': 'form-select, mb-3'}),
            'featured_image': forms.FileInput(attrs={
                'class': "form-control, mb-3",
                'type': "file"
                }),
        }


# Create a Recipe Form
class UpdateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'recipe_title',
            'category',
            'featured_comment',
            'recipe_ingridients',
            'recipe_instructions',
            'excerpt',
            'featured_image',
            )
        
        widgets = {
            'recipe_title': forms.TextInput(attrs={
                'class': 'form-control, mb-3',
                'placeholder': 'Type in Recipe Title'
                }),
            'category': forms.Select(attrs={
                'class': 'form-select-lg, mb-3'
                }),
            'featured_comment': forms.TextInput(attrs={
                'class': 'form-control, mb-3'
                }),
            'recipe_ingridients': SummernoteWidget(attrs={
                'summernote': {
                    'width': '100%',
                    'height': '300px',
                    'placeholder': 'Type in ingridients here...'
                    }
                }),
            'recipe_instructions': SummernoteWidget(attrs={
                'summernote': {
                    'width': '100%',
                    'height': '300px',
                    'placeholder': 'Provide instructions here...'
                    }
                }),
            'excerpt': forms.TextInput(attrs={
                'class': 'form-control, mb-3',
                'placeholder': 'Additional info info (e.g. nutrition facts etc.) as required go here...'
                }),
            'author': forms.Select(attrs={'class': 'form-select, mb-3'}),
            'featured_image': forms.FileInput(attrs={
                'class': "form-control, mb-3",
                'type': "file"
                }),
        }
