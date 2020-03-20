from django.http import HttpResponse
from django.template import loader

from .models import Card


def index(request):
    cards = Card.objects.all()

    template = loader.get_template('cards/index.html')

    context = {
        'cards': cards,
    }
    return HttpResponse(template.render(context, request))


def detail(request, card_id):
    return HttpResponse("Hello World! You are looking at card id: %s}" % card_id)
