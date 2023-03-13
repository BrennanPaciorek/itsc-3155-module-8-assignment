from flask.testing import FlaskClient
from src.models.movie import Movie

def test_create_movies_page(test_app: FlaskClient):
    response = test_app.post('/movies', data={
        "name": "Star Wars",
        "director": "George Lucas",
        "ratingOptions": "5"
    })

    assert response.status_code == 302

