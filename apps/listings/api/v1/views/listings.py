from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.commons.mixins.viewsets import ListCreateRetrieveDestroyViewSetMixin, ListCreateUpdateRetrieveViewSetMixin, \
    DestroyViewSetMixin
from apps.listings.models import Listing, PropertyType
from apps.realtors.models import Realtor

from ..serializer.listings import ListingSerializer


class ListingViewSet(ListCreateUpdateRetrieveViewSetMixin, DestroyViewSetMixin):
    permission_classes = AllowAny,
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()
