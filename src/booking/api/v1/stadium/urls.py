from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StadiumViewSet, StadiumImageViewSet
router = DefaultRouter()
router.register(r"", StadiumViewSet)
router.register(r"image", StadiumImageViewSet)
urlpatterns = [
    path('', include(router.urls)),
]