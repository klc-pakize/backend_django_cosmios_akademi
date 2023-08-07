from django.urls import path

from .views import RegisterView, logout

from rest_framework.authtoken import views

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path('login/', views.obtain_auth_token),
    path("logout/", logout)
]



