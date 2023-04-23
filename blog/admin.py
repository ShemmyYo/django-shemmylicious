from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Category, Comment, Profile


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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['category_name', 'status', 'featured_image']
    list_display = ('category_name', 'status', 'featured_image')
    actions = ['approve_category', 'reject_category']

    def approve_category(self, request, queryset):
        queryset.update(status=True)

    def reject_category(self, request, queryset):
        queryset.update(status=False)


admin.site.register(Profile)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['recipe_name', 'comment_title', 'email', 'active']
    list_display = ('recipe_name', 'created_date', 'active')
    list_filter = ('active', 'created_date')

    def approve_comment(self, request, queryset):
        queryset.update(active=True)

    def reject_comment(self, request, queryset):
        queryset.update(active=False)