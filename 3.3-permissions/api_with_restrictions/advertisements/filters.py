from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    status = filters.CharFilter(field_name='status')
    in_between = filters.DateFromToRangeFilter(field_name='created_at', lookup_expr='exact', label='in_between')
    created_by = filters.CharFilter(field_name='creator__username', lookup_expr='exact', label='creator')
    creator = filters.NumberFilter(field_name='creator__id')
    created_at_before = filters.DateFilter(field_name='created_at', lookup_expr='lte')
    created_at_after = filters.DateFilter(field_name='created_at', lookup_expr='gte')

    class Meta:
        model = Advertisement
        fields = {
            'status': ['exact'],
            'created_at': ['gt', 'lt', ],
            'creator': ['exact'],
        }