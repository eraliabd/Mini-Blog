from django.urls import path, include
from rest_framework import routers

from .views import AuthorViewSet

router = routers.DefaultRouter()

router.register('author', AuthorViewSet, basename='author')

urlpatterns = [
    path('', include(router.urls))
]
