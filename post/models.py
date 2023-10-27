from django.db import models
from users.models import Author

from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=250)
    icon = models.ImageField(upload_to='category_icon/')

    def __str__(self):
        return self.name


class Post(models.Model):
    # relations
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    comment = models.ManyToManyField('Comment')
    tag = models.ManyToManyField('Tag')

    # fields
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='post_image/')
    view_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish_time = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.CharField(max_length=250)
    email = models.EmailField(max_length=65)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user


class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
