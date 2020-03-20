from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url("^$", views.index, name="index"),
    path("card/<int:cards_id>/", views.detail, name="detail"),
]
