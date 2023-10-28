from django.db import models
from users.models import Author

from ckeditor.fields import RichTextField

import readtime


class Category(models.Model):
    name = models.CharField(max_length=250)
    icon = models.ImageField(upload_to='category_icon/')

    def __str__(self):
        return self.name


class Post(models.Model):
    # relations
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_posts')
    tag = models.ManyToManyField('Tag')

    # fields
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='post_image/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish_time = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)

    is_popular = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    order = models.IntegerField(default=0)

    class Meta:
        ordering = [
            'order',
            'created_at'
        ]

    def __str__(self):
        return self.title

    def get_readtime(self):
        result = readtime.of_text(self.content)
        return result.text


class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Comment(models.Model):
    # relations
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)

    # fields
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=65)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
