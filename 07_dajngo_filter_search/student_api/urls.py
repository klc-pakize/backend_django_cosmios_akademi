from django.urls import path, include

from rest_framework import routers

from .views import home, StudentMVS, PathMVS

router = routers.DefaultRouter()
router.register("student", StudentMVS)  # student/ - student/<int:pk>/ 
router.register("path", PathMVS)  # path/ - path/<int:pk>/ 

urlpatterns = [
    path("", home),
    #! ViewSets
    path("", include(router.urls)),

]

# urlpatterns += router.urls