from django.db import models
from django.utils import timezone

class Post(models.Model):
    name=models.CharField(max_length=20)
    res=models.TextField()
    emaill=models.EmailField()
    pdate=models.TextField(default=timezone.now())
    def __str__(self):
        return self.name