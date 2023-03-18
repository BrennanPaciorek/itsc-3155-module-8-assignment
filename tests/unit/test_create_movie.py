# TODO: Feature 2
from src.repositories.movie_repository import movie_repository
from src.models.movie import Movie

def test_create_movie():
    movie = movie_repository.create_movie('Paul Blaurt the mall cop','carson jacobus',3)

    assert type(movie) == Movie
    assert movie.title == 'Paul Blaurt the mall cop'
    assert movie.directior == 'carson jacobus'
    assert movie.rating == 3
    assert movie_repository.get_movie_by_title('Paul Blaurt the mall cop') != None