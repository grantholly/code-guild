from django.contrib import admin

from django.contrib.admin import ModelAdmin
from django_markdown.admin import MarkdownModelAdmin

from . import models


class BlogPostAdmin(MarkdownModelAdmin):
    list_view = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(ModelAdmin):
    list_view = ("blog, body")

admin.site.register(models.BlogPost, BlogPostAdmin)
admin.site.register(models.Comment, CommentAdmin)
