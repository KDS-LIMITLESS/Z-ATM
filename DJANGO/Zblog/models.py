from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    post = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    body = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    active= models.BooleanField(default=False)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'Comment by {self.username}'

