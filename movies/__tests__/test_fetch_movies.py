from movies.fetch_movies import process_data


def test_transform_films_data():
    films_data = [
        {
            "id": "id-castle-in-the-sky",
            "title": "Castle in the Sky",
            "description": "Description Castle in the Sky",
        },
    ]
    characters_data = [
        {
            "id": "id-pazu",
            "name": "Pazu",
            "films": ["https://ghibliapi.herokuapp.com/films/id-castle-in-the-sky"],
        },
    ]

    assert process_data(films_data, characters_data) == {
        "Castle in the Sky": [{"id": "id-pazu", "name": "Pazu"}],
    }
