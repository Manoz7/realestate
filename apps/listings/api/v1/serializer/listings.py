import re
from apps.commons.serializers import DynamicFieldsModelSerializer

from rest_framework import serializers
from django.conf import settings
from django.templatetags.static import static

from ....models import PropertyType, Listing, ListingImage


class ListingBaseSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=50)
    price = serializers.CharField(max_length=10)
    type = serializers.ListField()


class ListingGetSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Listing
        fields = ("title", "property_id", "description", "area")
        read_only_fields = 'uuid'


class ListingImageSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ListingImage
        fields = ('uuid', 'listing', 'image', 'order')
        read_only_fields = ('uuid', 'listing')


class ListingSerializer(DynamicFieldsModelSerializer):
    # admin_email = serializers.EmailField(write_only=True)
    images = ListingImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True)

    class Meta:
        model = Listing
        read_only_fields = ['property_id', 'uuid']
        fields = ['title', 'address', 'property_type', 'state', 'zipcode', 'description', 'property_face',
                  'build_year', 'price', 'bedrooms', 'bathroom', 'garage', 'floors', 'area',
                  'images', 'thumbnail', 'status', "uploaded_images"] + read_only_fields

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        listing = Listing.objects.create(**validated_data)
        for image in uploaded_images:
            new_image = ListingImage.objects.create(listing=listing, image=image)
        return listing

    # def get_fields(self):
    #     fields = super(ListingSerializer, self).get_fields()
    #     if fields.get('images'):
    #         fields['images'] = ListingImageSerializer(fields=['uuid', 'image', 'order'], many=True)
    #
    #     return fields

    # def get_image(self, obj):
    #     if not obj.listing_images.exists():
    #         import urllib.parse
    #         return urllib.parse.urljoin((getattr(settings, 'BACKEND_URL')), static('defaults/default_listings.jpg'))
    #     return self.request.build_absolute_uri(obj.listing_images.first().image.url)


# class ListingImageSerializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = ListingImage
#         fields = ('uuid', 'listing', 'image', 'order')
#         read_only_fields = ('uuid', 'listing')
#

class ListingImageUploadSerializer(serializers.Serializer):
    def validate(self, attrs):
        images = self.context.get('request').FILES
        if images.__len__() > 5:
            raise serializers.ValidationError('Cannot upload more than 5 photos')
        _images = []
        for _image in images.items():
            valid_extensions = ['jpg', 'jpeg', ' png']
            form_key = _image[0]
            _img_file = _image[1]
            ext = _image[1].name.split('.')[-1]
            print(ext)
            order_str = re.findall(r'\d+', form_key)[0]
            if not order_str.isdigit():
                raise serializers.ValidationError({form_key: "Invalid field"})
            int_order = int(order_str)
            if int_order > 5:
                raise serializers.ValidationError({form_key: "Cannot upload more images than placeholders"})
            if ext not in valid_extensions:
                raise serializers.ValidationError({form_key: "Not a valid image"})
            _images.append(dict(
                image=_img_file,
                order=int_order
            )
            )
        attrs.update(
            images=_images
        )
        print(attrs)
        return attrs
