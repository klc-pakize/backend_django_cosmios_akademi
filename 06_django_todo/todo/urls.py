from django.urls import path, include

from .views import todo_list_create, todo_get_update_delete, Todos, TodoDetail, MixTodo

from rest_framework import routers

router = routers.DefaultRouter()
router.register("todo", MixTodo)

urlpatterns = [
    path("list-create/", todo_list_create),
    path("detail/<int:pk>/", todo_get_update_delete),
    path("todo-list-create/", Todos.as_view()),
    path("todo-update-delete/<int:id>/", TodoDetail.as_view()),
    path("", include(router.urls)),
]