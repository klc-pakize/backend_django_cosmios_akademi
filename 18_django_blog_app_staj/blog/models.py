from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length = 35)

    def __str__(self):
        return self.name
    


class Blog(models.Model):

    STATUS = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )


    title = models.CharField(max_length= 100, unique=True)
    content = models.TextField(blank=True)
    image = models.ImageField(blank= True, null= True)
    cotegory = models.ForeignKey(Category, on_delete= models.CASCADE, related_name='blog')
    publish_date = models.DateTimeField(auto_now_add= True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    status = models.CharField(max_length=5, choices=STATUS, default='d', blank=True)

    def __str__(self):
        return f"{self.title} - {self.status}"
    


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="user_post_comments")
    blog = models.ForeignKey(Blog, on_delete= models.CASCADE, related_name="comments")
    content = models.CharField(max_length= 150)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="user_likes")
    blog = models.ForeignKey(Blog, on_delete= models.CASCADE, related_name="likes_n")
    likes = models.BooleanField(default=False)


    
class PostViews(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="user_post_views")
    blog = models.ForeignKey(Blog, on_delete= models.CASCADE, related_name="post_views")
    time_stamp = models.DateTimeField(auto_now_add=True)
    post_view = models.BooleanField(default=False)
