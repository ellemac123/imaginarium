from django.urls import path
from django.conf.urls import url

from .views import decks, cards

urlpatterns = [
    url("^$", decks.index, name="index"),
    path("cards/<str:deck_cards>/", cards.index, name="cards_index"),
    path("cards/<str:deck_cards>/card/<int:cards_id>/", cards.detail, name="cards_detail"),
]
