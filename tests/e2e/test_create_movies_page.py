from flask.testing import FlaskClient
from src.repositories.movie_repository import _movie_repo

def test_create_movies_page(test_app: FlaskClient):
    response = test_app.post('/movies', data={
        "name": "Star Wars",
        "director": "George Lucas",
        "ratingOptions": "5"
    })

    assert response.status_code == 302
    assert response.request.path == "/movies"
    assert _movie_repo.get_movie_by_title('Star Wars') !=  None

