from src.repositories.movie_repository import get_movie_repository as mr
from src.models.movie import Movie

def test_create_movie():
    title1 = "Star Wars"
    director1 = "George Lucas"
    rating1 = 5

    movie1 = Movie(title1, director1, rating1)
    test_movie = mr().create_movie(title1, director1, rating1)

    title2 = "Titanic"
    director2 = "James Cameron"
    rating2 = 4

    movie2 = Movie(title2, director2, rating2)

    assert test_movie.title == movie1.title
    assert test_movie.director == movie1.director
    assert test_movie.rating == movie1.rating

    assert test_movie.title != movie2.title
    assert test_movie.director != movie2.director
    assert test_movie.rating != movie2.rating

