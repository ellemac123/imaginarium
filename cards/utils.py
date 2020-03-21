import os

DECK_CHOICES = [
    ("original", "ORIGINAL"),
    ("persephone", "PERSEPHONE"),
    ("chimera", "CHIMERA"),
    ("pandora", "PANDORA"),
    ("odyssey", "ODYSSEY"),
]


def get_image_path(instance, filename):
    return os.path.join("photos", "cards", filename)
