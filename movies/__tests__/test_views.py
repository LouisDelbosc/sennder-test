from django.test import Client


def test_movies_index():
    c = Client()
    response = c.get("/movies/")
    assert response.status_code == 200
