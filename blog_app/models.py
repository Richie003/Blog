from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(default="", max_length=150, blank=False)
    article = models.TextField(default="", max_length=1000, blank=False)
    author = models.CharField(default="", max_length=100, blank=False)
    description = models.CharField(default="", max_length=150, blank=False)
    image = models.ImageField(upload_to='post_image/', blank=True, null=True)
    secondary_image = models.URLField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField(default="", max_length=1000, blank=False)
    comment_author = models.CharField(default="", max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(f"{self.comment_author} {self.created}")