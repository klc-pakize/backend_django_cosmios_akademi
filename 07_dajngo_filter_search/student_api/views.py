from django.shortcuts import render
from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer
from .paginations import CustomPageNumberPagination, CustomLimitOffsetPagination, CustomCursorPagination

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

@api_view(['GET'])
def home(request):
    return Response({
        'home':'Home Page'
    })

#! ViewSets

class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = CustomPageNumberPagination
    # pagination_class = CustomLimitOffsetPagination
    # pagination_class= CustomCursorPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['first_name', 'path']
    search_fields = ['first_name', 'last_name']

class PathMVS(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['path_name']