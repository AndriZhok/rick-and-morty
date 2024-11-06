from sqlite3 import IntegrityError

import requests

from characters.models import Characters
from rick_and_morty_apy import settings


def scrape_characters() -> list[Characters]:
    next_url_to_scrape = settings.RICK_AND_MORTY_APY_CHARACTERS

    characters = []

    while next_url_to_scrape is not None:
        characters_response = requests.get(next_url_to_scrape).json()
        for character_dict in characters_response["results"]:
            characters.append(
                Characters(
                    api_id=character_dict["id"],
                    name=character_dict["name"],
                    status=character_dict["status"],
                    species=character_dict["species"],
                    gender=character_dict["gender"],
                    image=character_dict["image"],
                )
            )

        next_url_to_scrape = characters_response["info"]["next"]

    return characters


def save_characters(characters: list[Characters]) -> None:
    for character in characters:
        try:
            character.save()
        except IntegrityError:
            print("User with api id {} already exists".format(character.api_id))


def sync_characters_with_api() -> None:
    characters = scrape_characters()
    save_characters(characters)
