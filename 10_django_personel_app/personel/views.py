from django.shortcuts import render

from .serializers import DepartmanSerializer, PersonelSerializer, DepartPersonelSerializer
from .models import Departman, Personel
from .permissions import IsStaffOrReadOnly, IsOwnerAndStaffOrReadOnly

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class DepartmanListCreateView(ListCreateAPIView):
    queryset = Departman.objects.all()
    serializer_class = DepartmanSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]


class PersonelListCreateView(ListCreateAPIView):
    queryset = Personel.objects.all()
    serializer_class = PersonelSerializer
    permission_classes = [IsStaffOrReadOnly, IsAuthenticated]

class PersonelRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Personel.objects.all()
    serializer_class = PersonelSerializer
    permission_classes = [IsAuthenticated, IsOwnerAndStaffOrReadOnly]

class DerpartmanPersonelView(ListAPIView):
    serializer_class = DepartPersonelSerializer
    queryset = Departman.objects.all()

    def get_queryset(self):
        name = self.kwargs['departman']

        return Departman.objects.filter(name__iexact=name)
