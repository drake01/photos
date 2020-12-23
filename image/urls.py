from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageViewSet, AlbumViewSet, UserViewSet

router = DefaultRouter()
router.register(r'image', ImageViewSet)
router.register(r'album', AlbumViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
