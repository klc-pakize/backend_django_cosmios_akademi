from django.shortcuts import render

from .models import Comment, Category, Likes, PostViews, Blog
from .serializers import CategorySerializer, BlogSerializer, CommentSerializer, LikesSerializer, PostViewSerializer, UserBlogSerializer
from .permissions import IsStaffOrReadOnly, IsOwnerOrReadOnly, IsOwnerOrReadOnlyComment

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

# Create your views here.

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]


class BlogView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsOwnerOrReadOnly]

    #! Blog sayfasının detayına girdiğimizde post_view create edilecek:
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        view_query = PostViews.objects.filter(user = request.user,  blog = instance)
        if not view_query.exists():
            PostViews.objects.create(user = request.user, blog = instance, post_view = True)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    #! Kullanıcı eğer blog sahibi ya da staff ise bloglarının status'u 'd' olsa bile görüntüleyip düzenleyebilecek:
    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()  # ==  Blog.objects.all()
        if super().get_queryset().filter(user = self.request.user.id):  # Blog.objects.filter(user = self.request.user.id)
            a = super().get_queryset().filter(user = self.request.user.id)  
            b = super().get_queryset().filter(status = 'p')
            return a | b
            # return super().get_queryset() 
        else:
           return super().get_queryset().filter(status = 'p')
    #! Kullanı staff ise BlogSerializer kullansın değil ise UserBlogSerializer'ı kullansın:
    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.request.user.is_staff:
            return serializer
        return UserBlogSerializer



class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnlyComment]

class LikesView(ModelViewSet):
    queryset = Likes.objects.filter(likes = True)
    serializer_class = LikesSerializer

class PostViewsView(ModelViewSet):
    queryset = PostViews.objects.all()
    serializer_class = PostViewSerializer