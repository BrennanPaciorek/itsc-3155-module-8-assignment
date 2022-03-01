# Please run pytest from project root directory
import sys
from pathlib import Path
sys.path.append(str(Path().resolve()))
from src.repositories.movie_repository import movie_repository_singleton
from src.models.movie import Movie


def test_get_all_movies_method():
    movies = [Movie("Spiderman", "Sam Raimi", 3), Movie("Spiderman 2", "John Watts", 4), Movie("Popular Movie", "Director Person", 1)]
    movie_repository_singleton.create_movie("Spiderman", "Sam Raimi", 3)
    movie_repository_singleton.create_movie("Spiderman 2", "John Watts", 4)
    movie_repository_singleton.create_movie("Popular Movie", "Director Person", 1)
    singleton_movies = movie_repository_singleton.get_all_movies()
    for movie in range(3):
        assert singleton_movies[movie].title == movies[movie].title
        assert singleton_movies[movie].director == movies[movie].director
        assert singleton_movies[movie].rating == movies[movie].rating

