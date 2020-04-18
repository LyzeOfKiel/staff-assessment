from django.conf import settings
from rest_framework import viewsets
from django.contrib.auth.models import Group
from rest_framework_simplejwt import authentication
from rest_framework.decorators import permission_classes

from .models import FeedbackDefault, Course
from .serializers import FeedbackDefaultSerializer, CourseSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = FeedbackDefault.objects.all()
    serializer_class = FeedbackDefaultSerializer
    authentication_classes = [authentication.JWTAuthentication]

    def create(self, request, *args, **kwargs):
        if 'student' not in request.data:
            request.data['student'] = request.user.id
        return super().create(request, *args, **kwargs)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [authentication.JWTAuthentication]
