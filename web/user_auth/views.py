from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from rest_framework import (
    response,
    permissions,
    status,
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes

from .serializers import UserCreateSerializer


User = get_user_model()


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def registration(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return response.Response(
            serializer.errors,
            status.HTTP_400_BAD_REQUEST
        )
    user = serializer.save()
    group_name = request.data["user_type"]

    # TODO assert group name is allowed

    # Assign user to group
    group, created = Group.objects.get_or_create(name=group_name)
    group.user_set.add(user)

    refresh = RefreshToken.for_user(user)
    res = {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
    return response.Response(res, status.HTTP_201_CREATED)
