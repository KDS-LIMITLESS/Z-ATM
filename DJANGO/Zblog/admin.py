from django.contrib import admin
from . import models

admin.site.register(models.Comment)
admin.site.register(models.RegisterUser)
admin.site.register(models.PasswordReset)
admin.site.register(models.LoginUser)


# Register your models here.
