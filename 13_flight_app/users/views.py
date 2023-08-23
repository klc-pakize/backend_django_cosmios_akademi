from django.shortcuts import render
from django.contrib.auth.models import User

from .serializers import RegisterSerializer

from rest_framework.generics import CreateAPIView
# Create your views here.

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

