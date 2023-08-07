from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer
from .permissions import IsAdminOrReadOnly
# Create your views here.

class CategoryMVS(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['name']
    permission_classes = [IsAdminOrReadOnly]


class PostMVS(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_fields = ['category__name']
    search_fields = ['title']
    permission_classes = [IsAuthenticatedOrReadOnly]