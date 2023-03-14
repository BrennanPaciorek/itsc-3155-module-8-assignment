# TODO: Feature 2
from src.repositories.movie_repository import movie_repository_singleton
from src.models.movie import Movie

def test_create_movies(test_app):
    my_dict = {
        'title': 'Kevin and Keiko',
        'director': 'Raul Calcamo',
        'rating': '5'
    }
    response = test_app.post('/movies', data=my_dict)

    assert movie_repository_singleton.get_movie_by_title('Kevin and Keiko') != None
    assert response.status_code == 302
    assert response.request.path == "/movies"
    