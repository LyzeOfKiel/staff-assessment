from rest_framework.routers import DefaultRouter

from .views import FeedbackViewSet, CourseViewSet

router = DefaultRouter()
router.register(r'feedback', FeedbackViewSet)
router.register(r'', CourseViewSet)

urlpatterns = router.urls
