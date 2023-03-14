from src.models.movie import Movie



class movierepo:
    movie_db = []
    def __init__(self):
        self.movie_db = [
            Movie("Fast and Furious", "Vin Diesal", 4),
            Movie("Creed", "Micheal B Jordan", 5),
            Movie("Rocky", "Sylvester Stallone", 5),
            Movie("SpiderMan", "Sam Raimi", 3),

            ]

    def get_all_movies(self):
        movie_to_string = []
        for movie in self.movie_db:
            movie_to_string.append(movie.toString())
        return movie_to_string

    def get_movie_by_title(self,title):
        for movie in self.movie_db:
            if movie.get_title() == title:
                return movie


    
