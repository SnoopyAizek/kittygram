from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CatViewSet, OwnerViewSet, FavoriteToyViewSet

router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
router.register('toy', FavoriteToyViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
