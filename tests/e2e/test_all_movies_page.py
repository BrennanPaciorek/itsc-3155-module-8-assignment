# TODO: Feature 1
import pytest

def test_list_all_movies(test_app):
    test_app.post('/movies',data=dict(title="Spiderman", director="Sam Raimi", rating="3"))
    test_app.post('/movies', data=dict(title="Spiderman 2",director="John Watts", rating="4"))
    test_app.post('/movies', data=dict(title="Popular Movie", director="Director Person", rating="1"))
    response = test_app.get('/movies')
    assert b"<tr><th>Spiderman</th><th>Sam Raimi</th><th>3/5</th></tr>" in response.data
    assert b"<tr><th>Spiderman 2</th><th>John Watts</th><th>4/5</th></tr>" in response.data
    assert b"<tr><th>Popular Movie</th><th>Director Person</th><th>1/5</th></tr>" in response.data
