from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceViewSet, UserDeviceViewSet

router = DefaultRouter()
router.register(r'devices', DeviceViewSet)
router.register(r'user-devices', UserDeviceViewSet, basename='user-devices')

urlpatterns = [
    path('', include(router.urls)),
]