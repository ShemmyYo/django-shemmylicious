from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Category


@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('recipe_ingridients', 'recipe_instructions')


admin.site.register(Category)

