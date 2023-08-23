from django.shortcuts import render

from .models import Flight, Reservation, Passenger
from .serializers import FlightSerializer, ReservationSerializer, StaffFlihgtSerializer
from .permissions import IsStaffOrReadOnly

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from datetime import date, datetime

# Create your views here.

class FlightView(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsStaffOrReadOnly]

    def get_serializer_class(self):
        serializer = super().get_serializer_class()  # == FlightSerializer

        if self.request.user.is_staff:
            return StaffFlihgtSerializer
        return serializer #  ==  FlightSerializer
    

    def get_queryset(self):
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        today = date.today()

        if self.request.user.is_staff:
            return Flight.objects.all()  # super().get_queryset()
        else:
            queryset = Flight.objects.filter(date_of_departure__gt = today)

            if Flight.objects.filter(date_of_departure = today):
                todat_queryset = Flight.objects.filter(estimated_time_of_departure__gt = current_time)

                queryset = queryset.union(todat_queryset)
        return queryset


class ReservationView(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()  # == Reservation.objects.all()

        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user = self.request.user)  # == Reservation.objects.filter(user = self.request.user)