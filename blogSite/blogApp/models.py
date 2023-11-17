from django.db import models

class RegisterModel(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=500)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class BlogModel(models.Model):
    blog_id = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    message = models.CharField(max_length=500)
    
