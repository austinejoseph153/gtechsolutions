from django.db import models
from django.contrib.auth.models import User
 



class PostField(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='title')
    slug = models.SlugField(max_length=150, unique=True, allow_unicode=True)
    author= models.ForeignKey(User, on_delete=models.RESTRICT,null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails')
    content = models.TextField(null=True, blank=True, verbose_name='body')
    read_time = models.IntegerField(null=True, blank=True)
    tags = models.ManyToManyField('techblog.Tag')
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id}. {self.title}' 
    
class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ['name']

        def __str__(self):
            return f'{self.id}. {self.name}'
        
class Comment(models.Model):

    post = models.ForeignKey(PostField, on_delete=models.CASCADE, verbose_name='post')
    author = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=True)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_created=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.id}. Comment by {self.author}'