class Movie:
    """A movie holds a title, director, and rating"""

    def __init__(self, title: str, director: str, rating: int):
        self.title = title
        self.director = director
        self.rating = rating

    def get_title(self):
        return self.title
    
    def toString(self):
        return "Title: " + self.title + " | Director: " + self.director + " | Rating: " + str(self.rating)
