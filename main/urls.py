from django.urls import path
from main.views import AirLineListView, AirLineDetailView, AirLineDeleteView, \
    AirLineCreateView, AirCraftDeleteView, AirCraftCreateView, AirLineFilterView

urlpatterns = [
    path('', AirLineListView.as_view(), name='airline-list'),
    path('airline/<int:pk>/', AirLineDetailView.as_view(), name='airline-detail'),
    path('airline-delete/<int:pk>/', AirLineDeleteView.as_view(), name='airline-delete'),
    path('airline-create/', AirLineCreateView.as_view(), name='airline-create'),
    path('aircraft-delete/<int:pk>', AirCraftDeleteView.as_view(), name='aircraft-delete'),
    path('airline/<int:pk>/aircraft-create/', AirCraftCreateView.as_view(), name='aircraft-create'),
    path('airline/<int:pk>/search/', AirLineFilterView.as_view(), name='airline-filter')
]
