from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class SignUp(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()

    def __unicode__(self):
	return smart_unicode(self.email)
