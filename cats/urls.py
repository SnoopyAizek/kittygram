from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CatViewSet, OwnerViewSet, FavoriteToyViewSet, LightCatViewSet

router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
router.register('toy', FavoriteToyViewSet)
router.register(r'mycats', LightCatViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
