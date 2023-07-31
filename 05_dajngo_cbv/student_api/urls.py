from django.urls import path, include

from rest_framework import routers

from .views import home, student_list, student_create, student_detail, student_update, student_delete, student_patch, StudentListCreate, StudentDetail, StudentGAV, StudentDetailGAV, StudentCV, StudentListCV, StudentCreateCV, StudentDetailCV, StudentMVS, PathMVS

router = routers.DefaultRouter()
router.register("student", StudentMVS)  # student/ - student/<int:pk>/ 
router.register("path", PathMVS)  # path/ - path/<int:pk>/ 

urlpatterns = [
    # path("", home),
    #! FUNCTİON VİEWS URL
    # path('student-list/', student_list),
    # path('student-create/', student_create),
    # path('student/<int:pk>/', student_detail),
    # path('student_update/<int:pk>/', student_update),
    # path('student_delete/<int:pk>/', student_delete),
    # path('student_patch/<int:pk>/', student_patch),

    #! CLASS VİEW URLS
    #! APIVIEW
    # path("student/", StudentListCreate.as_view()),
    # path("student/<int:pk>/", StudentDetail.as_view()),

    #! GENERICAPIView and Mixins
    # path('student/', StudentGAV.as_view()),
    # path('student/<int:pk>/', StudentDetailGAV.as_view()),

    #! Concrete Views
    # path("student/", StudentCV.as_view()),
    # path("student/list/", StudentListCV.as_view()),
    # path("student/create/", StudentCreateCV.as_view()),
    # path("student/<int:pk>/", StudentDetailCV.as_view()),


    #! ViewSets
    path("", include(router.urls)),

]

# urlpatterns += router.urls