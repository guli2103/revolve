from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post1(models.Model):
    name = models.ForeignKey(Post, on_delete = models.SET_NULL, null=True)
    context = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    img = models.CharField(max_length=255)

    def __str__(self):
        return self.context


class TopPost(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TopPost1(models.Model):
    name = models.ForeignKey(TopPost, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=255)
    slug = models.SlugField(null=False , unique=True)
    img = models.CharField(max_length=255) 
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name







    

