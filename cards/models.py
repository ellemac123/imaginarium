import os
import datetime
from django.db import models
from django.utils import timezone

DECK_CHOICES = [
    ('original', 'ORIGINAL'),
    ('persephone', 'PERSEPHONE'),
    ('chimera', 'CHIMERA'),
    ('pandora', 'PANDORA'),
    ('odyssey', 'ODYSSEY')
]


def get_image_path(filename):
    return os.path.join('photos', 'cards', filename)


class Deck(models.Model):
    identifier = models.CharField(max_length=30)
    deck = models.CharField(max_length=10, choices=DECK_CHOICES, default='original')


class Card(models.Model):
    identifier = models.CharField(max_length=30)
    date_added = models.DateTimeField('Date Added')
    picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __str__(self):
        return self.identifier

    def recently_added(self):
        return self.date_added >= timezone.now() - datetime.timedelta(days=2)

