from rest_framework import viewsets
from .serializers import CatSerializer, OwnerSerializer
from .models import Cat, Owner


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all().order_by('id')
    serializer_class = CatSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all().order_by('id')
    serializer_class = OwnerSerializer
