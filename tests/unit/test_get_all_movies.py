from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_get_all_movies():
    test_movie = get_movie_repository().create_movie("Star Wars", "George Lucas", 5)
    test_movie_list = []
    test_movie_list.append(test_movie)
    movies = get_movie_repository().get_all_movies()

    assert movies == test_movie_list
    assert movies[0] == test_movie_list[0]
    assert movies[0].title == test_movie_list[0].title

