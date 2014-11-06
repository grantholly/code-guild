from django.contrib import admin

from django_markdown.admin import MarkdownModelAdmin

from . import models
# Register your models here.


class BlogPostAdmin(MarkdownModelAdmin):
    list_view = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.BlogPost, BlogPostAdmin)
