from django.urls import path, include

from .views import home, product

urlpatterns = [

    path("", home), 
    path("products/", product), 
]