from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=220)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now_add=False, auto_now=False,
        default=timezone.now,null=True, blank=True)

    def __str__(self):
        return(self.title+'('+str(self.id)+')')