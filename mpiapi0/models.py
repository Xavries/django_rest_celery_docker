from django.db import models
from django.contrib.auth.models import User#, AbstractUser

class Upvote(models.Model):
    author_name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    upvoted_on = models.DateTimeField(auto_now_add=True)
    #id = models.IntegerField(primary_key=True)

#class User(AbstractUser):
#    id = models.IntegerField(primary_key=True)
#    bio=models.TextField()

class Post(models.Model):
    #id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=False, default='')
    #link = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    #upvotes_amount = models.IntegerField()
    upvotes_amount = models.ManyToManyField(User, blank=True, through=Upvote)
    author_name = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    content = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['creation_date']

class Comment(models.Model):
    author_name = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['creation_date']


