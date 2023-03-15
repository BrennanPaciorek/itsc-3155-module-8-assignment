from flask import Flask, redirect, render_template, request
# from src.repositories.movie_repository import get_movie_repository
import src.repositories.movie_repository as mod
import requests


app = Flask(__name__)


# movie_repository = get_movie_repository()
movie_repository = mod.movierepo()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True, db = movie_repository.get_all_movies())



@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)

@app.post('/movies')
def create_movie():
    title = request.form.get('title')
    director = request.form.get('director')
    rating = request.form.get('rating')
    #movie_repository_singleton.create_movie(title, director, rating)
    movie_repository.create_rating(title, director, rating)
    # After creating the movie in the database, we redirect to the list all movies page    
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    title = request.args.get("title")
   # mymovie = movie_repository_singleton.get_movie_by_title(title)
    mymovie = movie_repository.get_movie_by_title(title)
    return render_template('search_movies.html', search_active=True, mymovie=mymovie)
