from django.urls import path, include

from .views import CategoryView, BlogView, CommentView, LikesView, PostViewsView

from rest_framework import routers

router = routers.DefaultRouter()
router.register("categories", CategoryView)
router.register("blogs", BlogView)
router.register("comments", CommentView)
router.register("likes", LikesView)
router.register("post_view", PostViewsView)

urlpatterns = [

] + router.urls