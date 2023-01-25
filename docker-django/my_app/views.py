from django.shortcuts import render
from .models import student
from .serializer import studentSerializer
from rest_framework import viewsets


# Create your views here.
class studentViewset(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer