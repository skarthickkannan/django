from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title       = models.CharField(max_length=200)
    content     = models.TextField()
    slug        = models.SlugField(max_length = 250, null = True, blank = True)
    date_posted = models.DateTimeField(default=timezone.now)
    author      = models.ForeignKey(User, on_delete = models.CASCADE)
    image       = models.ImageField(upload_to='image_pics', default='def.jpg')
    likes       = models.ManyToManyField(User, related_name='blog_post')
    dislikes    = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    post        = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name        = models.CharField(max_length=80, default='Unknown')
    body        = models.TextField()
    created_on  = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
