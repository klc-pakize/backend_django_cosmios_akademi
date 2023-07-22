from django.urls import path
from cosmiosfs.views import home


urlpatterns = [
    path('home/', home),

]
