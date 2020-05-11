from rest_framework.routers import DefaultRouter
from django.urls import re_path

from .views import FeedbackCourseViewSet, FeedbackProfViewSet, \
    FeedbackTAViewSet, CourseViewSet, StudentViewSet, Stat, ProfViewSet, \
    TAViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')
router.register(r'feedback_course', FeedbackCourseViewSet)
router.register(r'feedback_prof', FeedbackProfViewSet)
router.register(r'feedback_ta', FeedbackTAViewSet)
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'profs', ProfViewSet, basename='profs')
router.register(r'tas', TAViewSet, basename='tas')


urlpatterns = [
    re_path('stats/', Stat.as_view()),
]

urlpatterns += router.urls
