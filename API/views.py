from .serializer import APIserializers
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import API
# Create your views here.
class GetAPI(generics.ListAPIView):
    queryset = API.objects.all()
    serializer_class = APIserializers
    permission_classes = (IsAdminUser,)
