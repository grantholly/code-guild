import datetime

from django.db import models


class DocumentActiveQuerySet(models.QuerySet):
    def is_active(self):
		return self.filter(active=True)


class Document(models.Model):
    """
    this class impelement a soft delete.  By marking the record inactive (active = False),
    it means that the file still exists in both the DB and the file system.
    Transaction rollbacks and DB restores will cause problems when looking for
    files no longer existing in the file system.
    """
    file_name = models.CharField(max_length=250, blank=True, null=True)
    document = models.FileField()
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    modified = models.DateTimeField(auto_now=True, null=True)
    user_title = models.CharField(max_length=250, blank=True, null=True)
    caption = models.CharField(max_length=250, blank=True, null=True)
    size = models.IntegerField()
    file_type = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(default=True)

    objects = DocumentActiveQuerySet.as_manager()

    def __unicode__(self):
	return self.document.name

    def get_file_type(self):
	return self.file_name[self.file_name.find("."):]

    def get_absolute_url(self):
	return self.document.url
