from django.urls import path

from .views import home, student_list, student_create, student_detail, student_update, student_delete, student_patch

urlpatterns = [
    path("", home),
    path('student-list/', student_list),
    path('student-create/', student_create),
    path('student/<int:pk>/', student_detail),
    path('student_update/<int:pk>/', student_update),
    path('student_delete/<int:pk>/', student_delete),
    path('student_patch/<int:pk>/', student_patch),

]