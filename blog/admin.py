from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Category, Comment


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('recipe_title',)}
    search_fields = ['recipe_title', 'email']
    list_display = ('recipe_title', 'category', 'author', 'status', 'updated_date')
    list_filter = ('status', 'created_date')
    actions = ['approve_comments', 'reject_comments']
    summernote_fields = ('recipe_ingridients', 'recipe_instructions')

    def approve_comments(self, request, queryset):
        queryset.update(status=True)

    def reject_comments(self, request, queryset):
        queryset.update(status=False)


admin.site.register(Category)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['recipe_name', 'comment_title', 'email']
    list_display = ('recipe_name', 'comment_title', 'email', 'created_date', 'active')
    list_filter = ('active', 'created_date')

