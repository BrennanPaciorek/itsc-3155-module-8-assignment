from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_create_movie():
    test_movie = get_movie_repository().create_movie("Star Wars", "George Lucas", 5)

    assert type(test_movie) == Movie
    assert test_movie.title == "Star Wars"
    assert test_movie.director == "George Lucas"
    assert test_movie.rating == 5