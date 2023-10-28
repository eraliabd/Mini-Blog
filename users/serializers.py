from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id', 'name', 'image', 'job', 'info', 'facebook_url', 'twitter_url', 'instagram_url', 'created_at',
        ]
