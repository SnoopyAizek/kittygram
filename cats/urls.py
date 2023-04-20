from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CatViewSet, OwnerViewSet

router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
