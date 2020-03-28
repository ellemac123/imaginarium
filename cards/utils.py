import os

DECK_CHOICES = [
    (1, "ORIGINAL"),
    (2, "PERSEPHONE"),
    (3, "CHIMERA"),
    (4, "PANDORA"),
    (5, "ODYSSEY"),
    (6, "ARIADNE"),
]


def get_image_path(instance, filename):
    return os.path.join("photos", "cards", filename)
