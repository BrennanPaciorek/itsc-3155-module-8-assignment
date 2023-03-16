import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from src.repositories.movie_repository import _movie_repo
from src.models.movie import Movie
#Used chatGPT to find out how to have access to the movie repo and get all movies function

def test_get_all_movies_method():
    movies = [Movie("Batman Begins", "Christopher Nolan", 4), Movie("Creed", "Ryan Coogler", 3), Movie("Django", "Quentin Tarantino", 4)]
    _movie_repo.create_movie("Batman Begins", "Christopher Nolan", 4)
    _movie_repo.create_movie("Creed", "Ryan Coogler", 3)
    _movie_repo.create_movie("Django", "Quentin Tarantino", 4)
    test_movies = _movie_repo.get_all_movies()
    for movie in range(3):
        assert type(test_movies[movie]) is Movie
        assert test_movies[movie].title == movies[movie].title
        assert test_movies[movie].director == movies[movie].director
        assert test_movies[movie].rating == movies[movie].rating