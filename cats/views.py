from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CatSerializer, OwnerSerializer, FavoriteToySerializer, CatListSerializer
from .models import Cat, Owner, FavoriteToy


class CreateRetrieveViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    pass


class LightCatViewSet(CreateRetrieveViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all().filter(
        is_purebred=True, deleted__isnull=True).order_by('-created')

    @action(detail=False, url_path='recent-white-cats')
    def recent_white_cats(self, request):

        cats = Cat.objects.filter(color='White').order_by('-birth_year')[:5]
        serializer = self.get_serializer(cats, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list':
            return CatListSerializer
        return CatSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all().order_by('id')
    serializer_class = OwnerSerializer


class FavoriteToyViewSet(viewsets.ModelViewSet):
    queryset = FavoriteToy.objects.all().order_by('id')
    serializer_class = FavoriteToySerializer
