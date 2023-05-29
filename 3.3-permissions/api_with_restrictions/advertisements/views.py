from rest_framework.viewsets import ModelViewSet
from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsAuthorOrReadOnly, IsAuthor
from advertisements.serializers import AdvertisementSerializer
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated


class AdvertisementViewSet(ModelViewSet):

    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    permission_classes = [IsAuthorOrReadOnly, ]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthor]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]