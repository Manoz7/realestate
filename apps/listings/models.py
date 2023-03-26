from django.db import models
from apps.realtors.models import Realtor
from apps.listings.constants import PROPERTY_FACE   , STATUS
from datetime import datetime
from django.core.exceptions import ValidationError

from apps.commons.models import BaseUUIDModel
# Create your models here.


class PropertyType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Listing(BaseUUIDModel):
    property_id = models.AutoField(primary_key=True, null=False)
    # realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, related_name='realtors')
    property_type = models.ForeignKey(PropertyType, on_delete=models.DO_NOTHING, to_field='name', default='Any',
                                      related_name='property_type')
    # city = models.ForeignKey(City, on_delete=models.DO_NOTHING, to_field='name', default='Any')
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=20, blank=True, default=44600)
    description = models.TextField(blank=True)
    property_face = models.CharField(max_length=20, choices=PROPERTY_FACE, default="P")
    build_year = models.DateField(null=True, blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField(default=0, blank=True)
    bathroom = models.IntegerField(default=0, blank=True)
    garage = models.IntegerField(default=0, blank=True)
    floors = models.IntegerField(default=0, blank=True)
    area = models.CharField(max_length=50)
    is_published = models.BooleanField(default=True)
    list_data = models.DateTimeField(default=datetime.now, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)  # for future use
    status = models.CharField(max_length=10, choices=STATUS, default="")

    @property
    def images(self):
        return self.listing_images

    def __str__(self):
        return self.title


class ListingImage(BaseUUIDModel):
    class Meta:
        ordering = ('order',)

    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='listing_images')
    image = models.ImageField()
    order = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.listing.title} --> {self.id}"
