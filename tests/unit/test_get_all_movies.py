from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_create_movie():
    test_movie = get_movie_repository().create_movie("Star Wars", "George Lucas", 5)

    movies = get_movie_repository().get_all_movies()

    assert type(movies) == list[movies]

