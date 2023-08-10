from django.urls import path
from .views import ProductListView,ProductCreateView,ProductUpdateView,ProductDeleteView,ProductRetriveView


urlpatterns = [
    path("",ProductListView.as_view()),
    path("<int:pk>/",ProductRetriveView.as_view()),
    path("create/",ProductCreateView.as_view()),
    path("<int:pk>/update/",ProductUpdateView.as_view()),
    path("<int:pk>/delete/",ProductDeleteView.as_view()),
]