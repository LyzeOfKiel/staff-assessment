from django.conf import settings
from rest_framework import viewsets
from django.contrib.auth.models import Group, User
from rest_framework_simplejwt import authentication
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import FeedbackDefault, Course
from .serializers import FeedbackDefaultSerializer, CourseSerializer, \
    StudentSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = FeedbackDefault.objects.all()
    serializer_class = FeedbackDefaultSerializer
    authentication_classes = [authentication.JWTAuthentication]

    def create(self, request, *args, **kwargs):
        course_name = request.data['course']
        matching_courses = Course.objects.filter(name=course_name)
        if matching_courses.count() == 1:
            request.data['course'] = matching_courses.first().pk
        if 'student' not in request.data:
            request.data['student'] = request.user.id
        return super().create(request, *args, **kwargs)


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    authentication_classes = [authentication.JWTAuthentication]

    def get_queryset(self):
        user = self.request.user

        if not user.is_anonymous:
            group = str(Group.objects.filter(user=user).first())
            if group == 'Student':
                return Course.objects.filter(students=user)
            else:
                return Course.objects

        return Course.objects


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = User.objects.filter(groups__name='Student')


class Stat(APIView):
    def get(self, request, format=None):
        feedbacks = FeedbackDefault.objects.all()
        serializer = FeedbackDefaultSerializer(feedbacks, many=True)
        data = serializer.data
        course_id_feeds = {}
        for f in data:
            c_id = f['course']
            if c_id not in course_id_feeds:
                course_id_feeds[c_id] = []
            course_id_feeds[c_id].append(f)
        course_rate = {}
        for c_id, feedback_list in course_id_feeds.items():
            rates = map(lambda f: f['rate'], feedback_list)
            course = Course.objects.get(pk=c_id)
            course_name = course.name
            course_rate[course_name] = sum(rates) / len(feedback_list)
        return Response(course_rate)
