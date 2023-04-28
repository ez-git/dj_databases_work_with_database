import datetime
from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=150,
                            null=False,
                            unique=True,
                            default='')
    price = models.FloatField(null=False, default=0.0)
    image = models.CharField(max_length=150, default='')
    release_date = models.DateField(null=False,
                                    default=datetime.date.today)
    lte_exists = models.BooleanField(null=False, default=False)
    slug = models.SlugField(max_length=150,
                            null=False,
                            blank=True,
                            unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Phone, self).save(*args, **kwargs)
