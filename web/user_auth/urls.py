from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import registration, UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('users/', include(router.urls)),
    # TODO rewrite as user creation
    path('register/', registration, name='register')
]
