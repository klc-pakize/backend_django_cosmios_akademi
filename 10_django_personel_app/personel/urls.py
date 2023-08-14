from django.urls import path

from .views import DepartmanListCreateView, PersonelListCreateView, PersonelRetrieveUpdateDeleteView, DerpartmanPersonelView

urlpatterns = [
    path("departman/", DepartmanListCreateView.as_view()),
    path('personel/', PersonelListCreateView.as_view()),
    path('personel/<int:pk>/', PersonelRetrieveUpdateDeleteView.as_view()),
    path('departman/<str:departman>/', DerpartmanPersonelView.as_view()),
]