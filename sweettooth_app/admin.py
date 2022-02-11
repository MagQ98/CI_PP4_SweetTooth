from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'author', 'created_on')
    search_fields = ['title', 'content', 'ingredients']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'ingredients', 'method')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
