from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    #post = models.ForeignKey('self', on_delete=models.CASCADE)
    #id = models.BigAutoField(auto_created=True, primary_key=True)
    username = models.CharField(max_length=15, default="username")
    email = models.EmailField(default='Your-email')
    body = models.TextField(default='Write your comments')
    date = models.DateTimeField(auto_now_add=True)
    active= models.BooleanField(default=False)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'Comment by {self.username}'

