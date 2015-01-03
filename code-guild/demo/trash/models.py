from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    document = models.FileField(upload_to="images/")

    def __unicode__(self):
	return self.document.name
