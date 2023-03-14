from src.repositories.movie_repository import movie_repository_singleton
from src.models.movie import Movie


def test_create_movie():
    movie = movie_repository_singleton.create_movie('Kevin and Keiko', 'Raul Calcamo', 5)

    assert type(movie) == Movie
    assert movie.title == 'Kevin and Keiko'
    assert movie.director == 'Raul Calcamo'
    assert movie.rating == 5
    assert movie_repository_singleton.get_movie_by_title('Kevin and Keiko') != None
