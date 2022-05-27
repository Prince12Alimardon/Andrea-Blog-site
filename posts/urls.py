from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('single/<slug:slug>/', single_post_view, name='single'),
    path('about/', about_view, name='about'),
    path('fashion/', fashion_view, name='fashion'),
    path('travel/', travel_view, name='travel'),
]
