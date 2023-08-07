from django.shortcuts import render
from django.contrib.auth.models import User

from .serializers import RegistrationSerializer

from rest_framework.generics import CreateAPIView

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({'message':'User logout, token deleted'})