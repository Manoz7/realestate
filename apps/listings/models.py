from django.db import models
from apps.realtors.models import Realtor
from apps.listings.constants import PROPERTY_CHOICES
from datetime import datetime

from apps.commons.models import BaseUUIDModel
# Create your models here.


class PropertyType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

#
# class City(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#
#     def __str__(self) -> str:
#         return self.name
#
#     class Meta:
#         verbose_name = "City"
#         verbose_name_plural = "Cities"


class Listing(BaseUUIDModel):
    property_id = models.AutoField(primary_key=True, null=False)
    # realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, related_name='realtors')
    property_type = models.ForeignKey(PropertyType, on_delete=models.DO_NOTHING, to_field='name', default='Any', related_name='property_type')
    # city = models.ForeignKey(City, on_delete=models.DO_NOTHING, to_field='name', default='Any')
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=20, blank=True, default=44600)
    description = models.TextField(blank=True)
    property_face = models.CharField(max_length=20, choices= PROPERTY_CHOICES, default="1")
    build_year = models.DateField()
    price = models.IntegerField()
    bedrooms = models.IntegerField(default=0, blank=True)
    bathroom = models.IntegerField(default=0, blank=True)
    garage = models.IntegerField(default=0, blank=True)
    floors = models.IntegerField(default=0, blank=True)
    area = models.CharField(max_length=50)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, default="default_house.jpg")
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, default="default_house.jpg")
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, default="default_house.jpg")
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, default="default_house.jpg")
    is_published = models.BooleanField(default=True)
    list_data = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

