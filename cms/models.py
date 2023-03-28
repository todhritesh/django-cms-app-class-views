from django.db import models
from tinymce.models import HTMLField 
from django.contrib.auth.models import User
  
class Category(models.Model):
    cat_name = models.CharField(max_length=50)
    cat_descr = models.TextField()

    def __str__(self):
        return self.cat_name
    
  
class Post(models.Model):
    title = models.CharField(max_length=100)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content =  HTMLField()
    createdAt = models.DateTimeField(auto_now=True, auto_now_add=False)
    updatedAt = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
    