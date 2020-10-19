import requests
from aiocache import cached
from collections import defaultdict


def process_data(raw_movies, raw_characters):
    characters = defaultdict(list)
    for char in raw_characters:
        for film_url in char["films"]:
            film_id = film_url.rsplit("/", 1)[1]
            characters[film_id].append({"id": char["id"], "name": char["name"]})
    return {movie["title"]: characters[movie["id"]] for movie in raw_movies}


@cached(ttl=60)
async def get_ghibli_data():
    raw_movies = requests.get("https://ghibliapi.herokuapp.com/films").json()
    raw_people = requests.get("https://ghibliapi.herokuapp.com/people").json()
    return process_data(raw_movies, raw_people)
