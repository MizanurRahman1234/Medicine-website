from django.urls import path
from .views import medicine_list_view

urlpatterns = [
    path('', medicine_list_view, name='medicine_list'),
]
