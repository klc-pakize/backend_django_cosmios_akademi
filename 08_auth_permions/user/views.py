from django.shortcuts import render

from .serializers import RegisterSerializer

from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# ----------- User Logout Function ------------------
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Kullanıcı Çıkış (Token Sil)
@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message": 'User Logout: Token Deleted'})