from django.contrib.auth.models import User
from django.db import models

from django_extensions.db.models import (ActivatorModel,
                                         TimeStampedModel)
from django_prices.models import PriceField
from geoposition.fields import GeopositionField
from tagulous.models import TagField

from market.apps.core.models import RandomSlugModel


class Post(RandomSlugModel, ActivatorModel, TimeStampedModel):
    UNIT_CHOICES = (
        ('pound', 'POUND'),
        ('gallon', 'GALLON'),
        ('each', 'EACH'),
    )

    owner = models.ForeignKey(User)

    # todo: published field
    # todo: Remove activatormodel?

    title = models.CharField(max_length=300)
    body = models.TextField(max_length=5000)

    # TODO: Use autocomplete_initial=True and specify preset tags
    tags = TagField(max_count=10, force_lowercase=True, space_delimiter=False)

    price = PriceField(currency='USD', max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=80, choices=UNIT_CHOICES, default='each')

    # location = models.CharField(max_length=5)
    location = GeopositionField()
