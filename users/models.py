from django.db import models
from django.contrib.auth import get_user_model

from ckeditor.fields import RichTextField

User = get_user_model()


class Author(models.Model):
    # relations
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    social_media = models.ManyToManyField('AuthorSocialMedia')

    # fields
    image = models.ImageField(upload_to='author_image/')
    job = models.CharField(max_length=250)
    info = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author


class SocialMedia(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField()

    def __str__(self):
        return self.name


class AuthorSocialMedia(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    social_media = models.ForeignKey(SocialMedia, on_delete=models.CASCADE)
