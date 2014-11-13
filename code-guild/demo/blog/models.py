from django.db import models


class BlogPostQuerySet(models.QuerySet):
    def published(self):
	return self.filter(published=True)


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=250, unique=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    objects = BlogPostQuerySet.as_manager()

    def __unicode__(self):
	return self.title

    class Meta:
	verbose_name = "Blog Post"
	ordering = ["-created"]

    
