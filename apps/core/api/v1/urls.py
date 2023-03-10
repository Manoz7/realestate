from django.urls import path
from rest_framework import routers

from .views.core import ContactViewSet

ROUTER = routers.DefaultRouter()

# ROUTER.register('demo', DemoViewSet, basename='demo-viewset')
ROUTER.register('contact', ContactViewSet, basename='contact-viewset')

urlpatterns = ROUTER.urls
