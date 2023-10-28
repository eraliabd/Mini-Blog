from django.db.models import Q, Count
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Category, Post, Comment, Tag
from .serializers import CategorySerializer, PostSerializer, TagSerializer, CommentSerializer

from users.models import Author
from users.serializers import AuthorSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostSearchViewList(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')

        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(category__icontains=search_query))
        return posts


class AuthorPostListView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        author_id = self.kwargs.get('pk')
        return Post.objects.filter(author_id=author_id)


class OurAuthorListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
