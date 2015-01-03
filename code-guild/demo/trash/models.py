import datetime

from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    document = models.FileField(upload_to="images/")
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    user_title = models.CharField(max_length=250, blank=True, null=True)
    caption = models.CharField(max_length=250, blank=True, null=True)

    def __unicode__(self):
	return self.document.name
