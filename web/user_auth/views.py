from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from rest_framework import (
    response,
    status,
    viewsets,
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import UserCreateSerializer, UserReadSerializer


User = get_user_model()


class RWSerializers(object):
    write_serializer_class = None
    read_serializer_class = None

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return self.write_serializer_class
        return self.read_serializer_class


class UserViewSet(RWSerializers, viewsets.ModelViewSet):
    queryset = User.objects.all()
    read_serializer_class = UserReadSerializer
    write_serializer_class = UserCreateSerializer

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAuthenticated, ]
        return super(self.__class__, self).get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return response.Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )
        user = serializer.save()

        group_name = request.data['user_type']

        # Assign user to group
        group, created = Group.objects.get_or_create(name=group_name)
        group.user_set.add(user)

        refresh = RefreshToken.for_user(user)
        res = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return response.Response(res, status.HTTP_201_CREATED)
