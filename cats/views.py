from rest_framework import viewsets
from .serializers import CatSerializer, OwnerSerializer, FavoriteToySerializer
from .models import Cat, Owner, FavoriteToy


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all().order_by('id')
    serializer_class = CatSerializer

    def list(self, request, *args, **kwargs):
        self.queryset = Cat.objects.all().filter(is_purebred=True, deleted__isnull=True).order_by('-created')
        return super().list(request, *args, **kwargs)


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all().order_by('id')
    serializer_class = OwnerSerializer


class FavoriteToyViewSet(viewsets.ModelViewSet):
    queryset = FavoriteToy.objects.all().order_by('id')
    serializer_class = FavoriteToySerializer
