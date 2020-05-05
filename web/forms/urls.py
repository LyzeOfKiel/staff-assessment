from rest_framework.routers import DefaultRouter
from django.urls import re_path

from .views import FeedbackCourseViewSet, FeedbackProfViewSet, \
    FeedbackTAViewSet, CourseViewSet, StudentViewSet, Stat

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'feedback_course', FeedbackCourseViewSet)
router.register(r'feedback_prof', FeedbackProfViewSet)
router.register(r'feedback_ta', FeedbackTAViewSet)
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    re_path('stats/', Stat.as_view()),
]

urlpatterns += router.urls
