from rest_framework.routers import DefaultRouter
from django.urls import re_path

from .views import FeedbackViewSet, CourseViewSet, StudentViewSet, Stat

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'feedback', FeedbackViewSet)
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    re_path('stats/', Stat.as_view()),
]

urlpatterns += router.urls
