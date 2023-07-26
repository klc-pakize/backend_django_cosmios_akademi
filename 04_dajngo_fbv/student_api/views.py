from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Student
from django.http import HttpResponse
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def home(request):
    return Response({
        'home':'Home Page'
    })


# GET (DB - veri çağırma)
# POST (DB - yeni bir veri create - pravite)
# PUT (DB - var olan veriyi update - pravite)
# PATCH (DB - var olan veriyi update - kısmı değişik - pravite)
# DELETE (DB - var olan veriyi silmek)


@api_view(['GET'])
def student_list(request):
    student = Student.objects.all()
    print(student)
    serializer = StudentSerializer(student, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message":"Datan DB kayıt edildi"
        }
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def student_detail(request, pk):
    student = get_object_or_404(Student, id = pk)
    # try:
    #     student = Student.objects.get(id = pk)
    # except:
    #     return Response({
    #         "message": "olmayan id numarası"
    #     })
    serializer = StudentSerializer(student)
    return Response(serializer.data)


@api_view(['PUT'])
def student_update(request, pk):
    student = get_object_or_404(Student, id = pk)
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def student_patch(request, pk):
    student = get_object_or_404(Student, id = pk)
    serializer = StudentSerializer(instance=student, data=request.data,  partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def student_delete(request, pk):
    student = get_object_or_404(Student, id = pk)
    student.delete()
    message = {
            "message":"Öğrenci silindi"
        }
    return Response(message)