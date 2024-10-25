# **Exercise 5: Movie Collection**

# - Create a dictionary where the keys are movie titles and the values are tuples containing the release year and rating.
# - Write a function that allows the user to search for a movie by title and returns the movie's details.
# - Allow the user to add, remove, or update movies in the collection using a loop.

from pprint import pprint

mov_dict = {
    "Scream 1": ("1996","7.3"),
    "Halloween 1": ("1978","6.7"),
    "Texas Chainsaw Massacre": ("1974","8.9"),
    "Friday the 13th": ("1980","8.5"),
}

def search_movie():
    
    movie_title = input("Please enter the movie title: ")
            
    if movie_title in mov_dict.keys():
        
        print(f"{movie_title} details: {mov_dict[movie_title]}")
        
    else:
        
        print(f"There's no movies called {movie_title} in our database.")
        
        
def add_movie():
    
    movie_title = input("Please enter the movie title: ")
    movie_release_date = int(input("Please enter the movie release year: "))
    movie_rating = float(input("Please enter the movie rating: "))
    
    mov_dict[movie_title] = (movie_release_date, movie_rating)
    
    pprint(mov_dict)

def rem_movie():
    
    movie_title = input("Please enter the movie (title) to remove: ")
    mov_dict.pop(movie_title)
    
    pprint(mov_dict)

def upd_movie():
    
    movie_title = input("Please enter the movie (title) to update: ")
    movie_release_date = int(input("Please enter the movie release year: "))
    movie_rating = float(input("Please enter the movie rating: "))
    
    mov_dict[movie_title] = (movie_release_date, movie_rating)
    pprint(mov_dict)

search_movie()
add_movie()
rem_movie()
upd_movie()