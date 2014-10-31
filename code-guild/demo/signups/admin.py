from django.contrib import admin

from .models import SignUp
# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
    class Meta:
	model = SignUp

admin.site.register(SignUp, SignUpAdmin)
