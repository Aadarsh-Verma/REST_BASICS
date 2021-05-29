from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    # slug = models.SlugField(unique=True,blank=True)

    def __str__(self):
        return self.title
#
# def pre_save_blog_post_receiever(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.author.username + "-" + instance.title)
#
#
# pre_save.connect(pre_save_blog_post_receiever, sender=Article)
