from django.urls import path

from .views import CatListApi, CatDetailApi

urlpatterns = [
    path('cats/', CatListApi.as_view()),
    path('cats/<int:pk>/', CatDetailApi.as_view()),
]
