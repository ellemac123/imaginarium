import os
from django.db import models


# Create your models here.
def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Card(models.Model):
    identifier = models.CharField(max_length=30)
    date_added = models.DateTimeField('Date Added')
    picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)
