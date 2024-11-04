from django.urls import path

from characters.views import get_random_characters, CharacterListView

app_name = "characters"

urlpatterns = [
    path("charecters/random/", get_random_characters, name="character_random"),
    path("charecters/", CharacterListView.as_view(), name="character_list"),
]
