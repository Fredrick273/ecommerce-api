from .views import UserListView,UserRegisterView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path("",UserListView.as_view()),
    path("register/",UserRegisterView.as_view()),
    path("login/",TokenObtainPairView.as_view()),
    path("login/refresh/",TokenRefreshView.as_view())
]