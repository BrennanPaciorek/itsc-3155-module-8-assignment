from flask.testing import FlaskClient
response = test_app.get('/movies')
    
def test_all_movies_page(test_app: FlaskClient):
    response = test_app.get('/movies')

    assert response,status_code == 200
    assert response.request.path == "/movies"
