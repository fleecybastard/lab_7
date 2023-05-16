import django_filters
from main.models import AirCraft


class AirCraftFilter(django_filters.FilterSet):
    class Meta:
        model = AirCraft
        fields = {
            'flight_distance': ['gt', 'lt']
        }
