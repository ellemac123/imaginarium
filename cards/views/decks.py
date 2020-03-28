from django.http import HttpResponse
from django.template import loader

from cards.models import Deck


def index(request):
    """
    The index page for the Card Model. This will call the index.html template
    that corresponds to the cards page.

    Args:
        request: the given request

    Returns: (HttpResponse) containing the rendered index template
    """
    decks = Deck.objects.all()

    template = loader.get_template("decks/index.html")

    context = {
        "decks": decks,
    }

    return HttpResponse(template.render(context, request))
