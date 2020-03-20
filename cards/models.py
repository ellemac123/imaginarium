import datetime
import os

from django.db import models
from django.utils import timezone

DECK_CHOICES = [
    ("original", "ORIGINAL"),
    ("persephone", "PERSEPHONE"),
    ("chimera", "CHIMERA"),
    ("pandora", "PANDORA"),
    ("odyssey", "ODYSSEY"),
]


def get_image_path(instance, filename):
    return os.path.join("photos", "cards", filename)


class Deck(models.Model):
    """
    A deck object will be one of the card deck choices. This may be removed in the future.
    """
    deck_name = models.CharField(max_length=30)
    deck = models.CharField(max_length=10, choices=DECK_CHOICES, default="original")

    def __str__(self):
        return self.deck_name


class Card(models.Model):
    """
    Create card objects that will hold the relevant features of a card and
    will contain and upload the image file
    """
    card_name = models.CharField(max_length=30)
    date_added = models.DateTimeField("Date Added")
    # TODO: Add a ImageField.height_field and ImageField.width_field for consistency of images
    picture = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __str__(self):
        return self.card_name

    def recently_added(self):
        return self.date_added >= timezone.now() - datetime.timedelta(days=2)
