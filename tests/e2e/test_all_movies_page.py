# TODO: Feature 1
def test_all_movies_page(test):
    test.post('/movies', data=dict(title="Batman Begins", director="Christopher Nolan", rating="4"))
    test.post('/movies', data=dict(title="Creed", director="Ryan Coogler", rating="3"))
    test.post('/movies', data=dict(title="Django", director="Quentin Tarantino", rating="4"))
    response = test.get('/movies')
    assert b"<tr><th>Batman Begins</th><td>Christopher Nolan</td><td>4</td></tr>" in response.data
    assert b"<tr><th>Creed</th><td>Ryan Coogler</td><td>3</td></tr>" in response.data
    assert b"<tr><th>Django</th><td>Quentin Tarantino</td><td>4</td></tr>" in response.data