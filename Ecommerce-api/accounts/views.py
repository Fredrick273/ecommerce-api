from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView, CreateAPIView
from .serilalizers import UserSerializer
from .models import UserData
from rest_framework import authentication,permissions


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = UserData.objects.all()
    # authentication_classes = [authentication.SessionAuthentication,authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

class UserRegisterView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = UserData.objects.all()
