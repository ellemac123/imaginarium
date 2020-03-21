from django.http import HttpResponse
from django.template import loader

from cards.models import Card


def index(request, deck_cards):
    """
    The index page for the Card Model. This will call the index.html template
    that corresponds to the cards page.

    Args:
        request: the given request

    Returns: (HttpResponse) containing the rendered index template
    """
    cards = Card.objects.get(deck=deck_cards)

    template = loader.get_template("cards/index.html")

    context = {
        "cards": cards,
    }
    return HttpResponse(template.render(context, request))


def detail(request, cards_id):
    """
    Detail page for a specific card. Will get the card based on the id and will
    render the detail template
    Args:
        request: the given request
        cards_id: (int) id corresponding to a Card object

    Returns: (HttpResponse) django template for the specific card object
    """

    card = Card.objects.get(id=cards_id)

    template = loader.get_template("cards/detail.html")

    context = {
        "card": card
    }

    return HttpResponse(template.render(context, request))
