from rest_framework import viewsets
from django.contrib.auth.models import Group, User
from rest_framework_simplejwt import authentication
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course, FeedbackCourse, FeedbackProf, FeedbackTA
from .serializers import FeedbackCourseGetSerializer, \
    FeedbackCoursePostSerializer, FeedbackProfSerializer, \
    FeedbackTASerializer, CourseSerializer, StudentSerializer


class RWSerializers(object):
    write_serializer_class = None
    read_serializer_class = None

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return self.write_serializer_class
        return self.read_serializer_class


class FeedbackCourseViewSet(RWSerializers, viewsets.ModelViewSet):
    queryset = FeedbackCourse.objects.all()
    read_serializer_class = FeedbackCourseGetSerializer
    write_serializer_class = FeedbackCoursePostSerializer
    authentication_classes = [authentication.JWTAuthentication]

    def create(self, request, *args, **kwargs):
        course_name = request.data['course']
        matching_courses = Course.objects.filter(name=course_name)
        if matching_courses.count() == 1:
            request.data['course'] = matching_courses.first().pk
        if 'student' not in request.data:
            request.data['student'] = request.user.id
        return super().create(request, *args, **kwargs)


class FeedbackProfViewSet(viewsets.ModelViewSet):
    queryset = FeedbackProf.objects.all()
    serializer_class = FeedbackProfSerializer
    authentication_classes = [authentication.JWTAuthentication]


class FeedbackTAViewSet(viewsets.ModelViewSet):
    queryset = FeedbackTA.objects.all()
    serializer_class = FeedbackTASerializer
    authentication_classes = [authentication.JWTAuthentication]


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    authentication_classes = [authentication.JWTAuthentication]

    def get_queryset(self):
        user = self.request.user

        if not user.is_anonymous:
            group = str(Group.objects.filter(user=user).first())
            if group == 'Student':
                return Course.objects.filter(students=user)
            elif group == 'Prof':
                return Course.objects.filter(prof=user)
            elif group == 'TA':
                return Course.objects.filter(tas=user)

        return Course.objects


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = User.objects.filter(groups__name='Student')


class Stat(APIView):
    def get(self, request, format=None):
        feedbacks = FeedbackDefault.objects.all()
        serializer = FeedbackPostSerializer(feedbacks, many=True)
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
