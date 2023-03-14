

def test_list_all_movies(test_app):
    test_app.post('/movies',data=dict(title="Spiderman", director="Sam Raimi", rating="3"))
    test_app.post('/movies', data=dict(title="Spiderman 2",director="John Watts", rating="4"))
    test_app.post('/movies', data=dict(title="Popular Movie", director="Director Person", rating="1"))
    response = test_app.get('/movies')
    assert b"<tr><th>Spiderman</th><td>Sam Raimi</td><td>3/5</td></tr>" in response.data
    assert b"<tr><th>Spiderman 2</th><td>John Watts</td><td>4/5</td></tr>" in response.data
    assert b"<tr><th>Popular Movie</th><td>Director Person</td><td>1/5</td></tr>" in response.data
