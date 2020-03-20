from django.http import HttpResponse

from .models import Card


def index(request):
    return HttpResponse("Hello World! You're at the cards index :)")


def detail(request, card_id):
    return HttpResponse("Hello World! You are looking at card id: %s}" % card_id)
