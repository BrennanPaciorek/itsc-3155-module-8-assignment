# TODO: Feature 3

from src.repositories.movie_repository import MovieRepository
from src.models.movie import Movie


def test_get_movie_by_title():
    mymovies = MovieRepository()

    assert None == mymovies.get_movie_by_title("The Dark Knight")

    mymovies.create_movie("The Dark Knight", "Christopher Nolan", 5)
    result_1 = mymovies.get_movie_by_title("The Dark Knight")

    assert result_1.title == "The Dark Knight"
    assert result_1.director == "Christopher Nolan"
    assert result_1.rating == 5
