from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import OrderItemViewSet,OrderViewSet

router = DefaultRouter()
router.register(r'order', OrderViewSet,basename='order')
router.register(r'orderitem', OrderItemViewSet,basename='orderitems')

urlpatterns = [
    path('', include(router.urls)),
]