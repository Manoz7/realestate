from django.urls import path
from rest_framework import routers

# from .views.demo import DemoView, DemoViewSet
from .views.listings import ListingViewSet

ROUTER = routers.DefaultRouter()

# ROUTER.register('demo', DemoViewSet, basename='demo-viewset')
ROUTER.register('', ListingViewSet, basename='listing-viewset')

urlpatterns = ROUTER.urls
