from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView, get_object_or_404
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser, JSONParser

from apps.commons.mixins.viewsets import ListCreateRetrieveDestroyViewSetMixin, ListCreateUpdateRetrieveViewSetMixin, \
    DestroyViewSetMixin


from apps.listings.models import Listing, PropertyType, ListingImage
from apps.realtors.models import Realtor
from ..serializer.listings import ListingSerializer, ListingImageSerializer, ListingGetSerializer, \
    ListingImageUploadSerializer


# def validate_images(data):
#     LISTING_IMAGE_LIMIT = 5
#     for _img in data:
#         pass


class ListingViewSet(ListCreateUpdateRetrieveViewSetMixin, DestroyViewSetMixin):
    queryset = Listing.objects.all()
    lookup_field = 'uuid'
    lookup_kwarg = 'uuid'
    permission_classes = AllowAny,
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filter_fields = ('address', 'price')
    search_fields = ('title', 'descriptions', 'price')
    ordering_fields = ('status', 'created_at', 'updated_at')
    serializer_class = ListingSerializer
    pagination_class = PageNumberPagination


    # def get_serializer_class(self):
    #     if self.action == 'add_image':
    #         return ListingImageUploadSerializer
    #     if self.action == 'update_image':
    #         return ListingImageSerializer
    #     return ListingSerializer

    # def get_serializer(self, *args, **kwargs):
    #     if self.action == "create":
    #         kwargs['fields'] = (
    #             'title', 'address', 'property_type', 'state', 'zipcode', 'description', 'property_face',
    #             'build_year', 'price', 'bedrooms', 'bathroom', 'garage', 'floors', 'area',
    #             'thumbnail', 'status'
    #         )
    #     if self.action == 'list':
    #         kwargs['fields'] = (
    #             'uuid', 'title', 'address', 'property_type', 'state', 'zipcode', 'description', 'property_face',
    #             'build_year', 'price', 'bedrooms', 'bathroom', 'garage', 'floors', 'area',
    #             'thumbnail', 'status', 'image'
    #         )
    #
    #     if self.action == 'retrieve':
    #         kwargs['fields'] = (
    #             'uuid', 'title', 'address', 'property_type', 'state', 'zipcode', 'description', 'property_face',
    #             'build_year', 'price', 'bedrooms', 'bathroom', 'garage', 'floors', 'area',
    #             'thumbnail', 'status', 'image'
    #         )
    #
    #     if self.action == 'update_image':
    #         kwargs['fields'] = ('image',)

    # @action(methods=['post'],
    #         detail=True,
    #         url_path='add-image',
    #         url_name='add_image')
    # def add_image(self, request, *args, **kwargs):
    #     self.parser_classes = (FileUploadParser, MultiPartParser)
    #     obj = self.get_object()
    #     ser = self.get_serializer(data=request.data)
    #     ser.is_valid(raise_exception=True)
    #     new_imgs = ser.validated_data['images']
    #     for _image_dict in new_imgs:
    #         try:
    #             _img_obj = obj.listing_images.get(
    #                 order=_image_dict.get('order')
    #             )
    #             _img_obj.image = _image_dict.get('image')
    #             _img_obj.save(update_fields=['image'])
    #         except:
    #             obj.listing_images.create(
    #                 **_image_dict
    #             )
    #     return Response(
    #         {'details': "successfully updated images"}
    #     )

    # @action(methods=['put'],
    #         detail=True,
    #         url_path='image/(?P<image_uuid>[^/.]+)/update',
    #         url_name='update_image')
    # def update_image(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     image_obj = get_object_or_404(
    #         obj.listing_images.all(), uuid=self.kwargs['image_uuid']
    #     )
    #     ser = self.get_serializer(data= request.data)
    #     ser.is_valid(raise_exception=True)
    #     image_obj.image = ser.validated_data
    #     image_obj.save(update_fields=['image'])
    #     return Response(
    #         {"detail": "Successfully updated image"}
    #     )
    #
    # @action(methods=['delete'],
    #         detail=True,
    #         url_path='image/(?P<image_uuid>[^/.]+)/delete',
    #         url_name='delete_image')
    # def delete_image(self):
    #     obj = self.get_object()
    #     image = get_object_or_404(
    #         obj.listing_images.all(), uuid=self.kwargs['image_uuid']
    #     )
    #     image.delete()
    #     return Response(
    #         {"detail": "Successfully deleted image"}
    #     )
