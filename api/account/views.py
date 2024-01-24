from django.shortcuts import render
from rest_framework import generics

from .models import User
from .serializers import SignUpSerializer, UserModelSerializer

# Create your views here.


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserSignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
