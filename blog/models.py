from django.db import models
from ckeditor.fields import RichTextField


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=65)
    subject = models.CharField(max_length=250, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class OurPage(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    logo = models.ImageField(upload_to='our_page_logo/')
    link = models.URLField()

    def __str__(self):
        return f"Name: {self.name}"


class FAQ(models.Model):
    question = RichTextField()
    answer = RichTextField()

    def __str__(self):
        return self.question
