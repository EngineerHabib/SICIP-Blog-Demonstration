from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserModel(AbstractUser):
    full_name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.full_name

class BlogModel(models.Model):
    CATEGORY_TYPES = [
        ('Educational','Educational'),
        ('Technologies','Technologies'),
        ('Sports','Sports'),
    ]
    title = models.CharField(max_length=150,null=True)
    author_name = models.CharField(max_length=100,null=True)
    content = models.TextField(null=True)
    category = models.CharField(choices=CATEGORY_TYPES,null=True)
    blog_image = models.ImageField(upload_to='media/blog_image',null=True)
    publish_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f'{self.author_name}'