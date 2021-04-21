from django.db import models


class RegisterUser(models.Model):
    firstName = models.CharField(max_length=15, null=False)
    lastName = models.CharField(max_length=15, null=False)
    otherNames = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(null=False, max_length=16)
    

    def save(self, *args,**kwargs):
        super().save() 

class LoginUser(models.Model):
    email = models.EmailField(null=False)
    password = models.CharField(max_length=16, null=False)


class PasswordReset(models.Model):
    email = models.EmailField(null=False)


class Comment(models.Model):
    comments = models.TextField(max_length=200)

