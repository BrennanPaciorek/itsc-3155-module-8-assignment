# TODO: Feature 2
from src.repositories.movie_repository import movie_repository
from src.repositories.movie_repository import Movie

def test_create_movies(test_app):
    test = {
        'title' : 'Paul Blaurt the mall cop',
        'director' : 'carson jacobus',
        'rating' : '3'
    }
    answer = test_app.post('/movies',data = test)

    assert movie_repository.get_movie_by_title('Paul Blaurt the mall cop') != None
    assert answer.status_code == 302
    assert answer.request.path == "/movies"
