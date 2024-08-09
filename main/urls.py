from django.urls import path
from .views import (
    HomeListView, MenuListView,
    ContactListView, TodayListView,
    filter_product,
)

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('menu/', MenuListView.as_view(), name='menu'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('today/', TodayListView.as_view(), name='today'),
    path('filter-products/', filter_product, name='filter-product'),
]



