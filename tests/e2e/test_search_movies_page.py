# TODO: Feature 3

from app import app
from src.repositories.movie_repository import movie_repository_singleton


def test_search_movies_page():
    test_app = app.test_client()

    response = test_app.get("/movies/search")
    assert b'<p>No Results</p>' in response.data

    response = test_app.get("/movies/search?title=The+ManBat")
    assert b'<p>No Results</p>' in response.data

    movie_repository_singleton.create_movie(
        "The Dark Knight", "Christopher Nolan", 5)

    response = test_app.get("/movies/search?title=The+Dark+Knight")

    assert b'<td>Result Found:</td>' in response.data
    assert b'<td>The Dark Knight</td>' in response.data
    assert b'<td>Star rating:</td>' in response.data
    assert b'<td>5</td>' in response.data
