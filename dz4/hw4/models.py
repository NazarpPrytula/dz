from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.CharField(max_length = 180)
    date = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.author

