from django.http import HttpResponse
from django.template import loader

from cards.utils import DECK_CHOICES


def index(request):
    """
    The index page for the Card Model. This will call the index.html template
    that corresponds to the cards page.

    Args:
        request: the given request

    Returns: (HttpResponse) containing the rendered index template
    """
    deck_categories = []

    for deck in DECK_CHOICES:
        deck_categories.append(deck)

    template = loader.get_template("decks/index.html")

    context = {
        "decks": deck_categories,
    }

    return HttpResponse(template.render(context, request))
