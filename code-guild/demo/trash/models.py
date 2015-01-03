import datetime

from django.db import models


class Document(models.Model):
    file_name = models.CharField(max_length=250, blank=True, null=True)
    document = models.FileField(upload_to="images/")
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    modified = models.DateTimeField(auto_now=True, null=True)
    user_title = models.CharField(max_length=250, blank=True, null=True)
    caption = models.CharField(max_length=250, blank=True, null=True)
    size = models.IntegerField()
    file_type = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
	return self.document.name

    def get_file_type(self):
	return self.file_name[self.file_name.find("."):]

    def get_absolute_url(self):
	return self.document.url
