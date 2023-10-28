from django.urls import path, include
from rest_framework import routers

from .views import CategoryViewSet, PostViewSet, TagViewSet, CommentViewSet, AuthorPostListView, OurAuthorListView

router = routers.DefaultRouter()

router.register('category', CategoryViewSet, basename='category')
router.register('post', PostViewSet, basename='post')
router.register('tag', TagViewSet, basename='tag')
router.register('comment', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('author-post-list/<int:pk>/', AuthorPostListView.as_view(), name='author-post-list'),
    path('author-post-count/', OurAuthorListView.as_view(), name='author-post-count'),
]
