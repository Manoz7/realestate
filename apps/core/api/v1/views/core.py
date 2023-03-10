from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.commons.mixins.viewsets import ListCreateRetrieveDestroyViewSetMixin, ListCreateUpdateRetrieveViewSetMixin, \
    DestroyViewSetMixin
from apps.core.models import Contact
from ..serializer.core import ContactSerializer


class ContactViewSet(ListCreateRetrieveDestroyViewSetMixin):
    permission_classes = AllowAny,
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()