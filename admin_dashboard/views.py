from rest_framework import viewsets
from users.models import CustomUser
from .serializers import UserSerializer, DeviceSerializer
from rest_framework import viewsets
from devices.models import Device
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
# from .models import UserAccessLog
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [AllowAny]



class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Only admins can manage users

    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['is_active', 'user_type', 'created_ip', 'email']  # Filter by active status, user type, etc.
    ordering_fields = ['date_joined', 'email', 'last_login']  # Sort by these fields
    ordering = ['-date_joined']  # Default ordering (newest first)

    @action(detail=True, methods=['post'], url_path='suspend')
    def suspend_user(self, request, pk=None):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response({'status': 'user suspended'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='reactivate')
    def reactivate_user(self, request, pk=None):
        user = self.get_object()
        user.is_active = True
        user.save()
        return Response({'status': 'user reactivated'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='reset-password')
    def reset_password(self, request, pk=None):
        user = self.get_object()
        user.send_password_reset_email()
        return Response({'status': 'password reset email sent'}, status=status.HTTP_200_OK)

# @receiver(user_logged_in)
# def log_user_login(sender, request, user, **kwargs):
#     UserAccessLog.objects.create(
#         user=user,
#         action='Login',
#         ip_address=request.META.get('REMOTE_ADDR')
#     )
