from django.db import models
import uuid
# Create your models here.


class BaseUUIDModel(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True
    )

    class Meta:
        abstract = True