from django.urls import path
from .views import (
    HomeListView, MenuListView,
    ContactListView, TodayListView,
)

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('menu/', MenuListView.as_view(), name='menu'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('today/', TodayListView.as_view(), name='today'),
]



