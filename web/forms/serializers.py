from django.contrib.auth.models import User

from rest_framework import serializers

from .models import FeedbackDefault, Course


class FeedbackDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackDefault
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'courses')
