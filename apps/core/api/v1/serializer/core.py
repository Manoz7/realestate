from apps.commons.serializers import DynamicFieldsModelSerializer

from rest_framework import serializers

from ....models import Contact


class ContactSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'subject', 'message']
