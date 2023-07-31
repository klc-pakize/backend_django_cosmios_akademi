from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Student, Path
from django.http import HttpResponse
from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, mixins
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

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

#!#################### FUNCTION BASED VIEWS ########################################

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


#!#################### CLASS BASED VIEWS ########################################
#! APIVIEW
class StudentListCreate(APIView):
    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            message = {
                "message":"Datan DB kayıt edildi"
            }
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetail(APIView):

    def get(self, request, pk):
        student = get_object_or_404(Student, id = pk)  # == Student.objects.get(id = pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self, request, pk):
        student = get_object_or_404(Student, id = pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requeset, pk):
        student = get_object_or_404(Student, id = pk)
        student.delete()
        message = {
                "message":"Öğrenci silindi"
            }
        return Response(message)



#! GENERICAPIView and Mixins
#? Mixins
# - ListModelMixin
#     - list method
# - CreateModelMixin
#     - create method
# - RetrieveModelMixin
#     - retrieve method
# - UpdateModelMixin
#     - update method
# - DestroyModelMixin
#     - destroy method 


class StudentGAV(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list( request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create( request, *args, **kwargs)
    

# class StudentCreateGAV(mixins.CreateModelMixin, GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def post(self, request, *args, **kwargs):
#         return self.create( request, *args, **kwargs)
    

class StudentDetailGAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

#! Concrete Views

class StudentCV(ListCreateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentListCV(ListAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreateCV(CreateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailCV(RetrieveUpdateDestroyAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


#! ViewSets

class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class PathMVS(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer