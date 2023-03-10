from apps.commons.serializers import DynamicFieldsModelSerializer

from rest_framework import serializers

from ....models import PropertyType, Listing


class ListingSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Listing
        read_only_fields = ['property_id']
        fields = ['title', 'address', 'property_type', 'state', 'zipcode', 'description', 'property_face',
                  'build_year', 'price', 'bedrooms', 'bathroom', 'garage', 'floors', 'area', 'photo_main', 'photo_1',
                  'photo_2', 'photo_3', 'photo_4'] + read_only_fields
