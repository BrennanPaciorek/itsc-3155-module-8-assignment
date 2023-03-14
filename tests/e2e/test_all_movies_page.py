response = test_app.get('/movies')
    
assert response,status_code == 200
assert response.request.path == "/movies"
