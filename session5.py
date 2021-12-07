##########################################################################################################
# Python lesson 5 - 2021.12.07
##########################################################################################################

# Before doing tasks:
# 1. Download file: https://github.com/ryszardnikiel/XXXI_python/blob/main/session5.json
# 2. Save downloaded file in the same folder as your python script

# To convert data from json file to python object:
import json
with open('session5.json') as f:  # open json file
    movies = json.load(f)  # create object movies which is the list of movies

# Tasks:
# 1. Check how many movies in a list
# 2. Check the structure of the first element
# 3. Create function 'get_best_movie' which returns movie with highest rank
# 4. Create function 'get_oldest_movie' which returns the oldest movie
# 5. Create function 'get_best_movie_type' which returns the best movie for provided movie genre e.g western
# 6. get the list of directors - each list element is one director


# Solutions:

# 1. Check how many movies in a list
print(f"There are {len(movies)} in the movies list")

# 2. Check the structure of the first element
print(movies[0])
# {'Title': 'Grave of the Fireflies',
#  'Year': 1988,
#  'Genre': 'Animation, Drama, War',
#  'Director': 'Isao Takahata',
#  'Writer': 'Akiyuki Nosaka, Isao Takahata',
#  'imdbRating': 8.4,
#  'imdbVotes': 76471}


# 3. Create function 'get_best_movie' which returns movie with highest rank
def get_best_movie(movies):
    rating = 0
    best_movie = {}
    for movie in movies:
        if movie['imdbRating'] > rating:
            best_movie = movie
            rating = movie['imdbRating']
    return best_movie


best_movie = get_best_movie(movies)
print(f"The best movie is {best_movie['Title']} created in {best_movie['Year']}")


# 4. Create function 'get_oldest_movie' which returns the oldest movie
def get_oldest_movie(movies):
    year = 2021
    oldest_movie = {}
    for movie in movies:
        if movie['Year'] < year:
            oldest_movie = movie
            year = movie['Year']
    return oldest_movie


oldest_movie = get_oldest_movie(movies)
print(f"The oldest movie is {oldest_movie['Title']} created in {oldest_movie['Year']}")


# 5. Create function 'get_best_movie_type' which returns the best movie for provided movie genre e.g western

# example to show how to check if some text is part of another text
if 'some' in 'some_text':
    print('text included')
else:
    print('text not included')


def get_best_movie_type(movies, genre):
    rating = 0
    best_movie = {}
    for movie in movies:
        if movie['imdbRating'] > rating and genre in movie['Genre']:
            best_movie = movie
            rating = movie['imdbRating']
    return best_movie


genre = 'Western'
print(f"The best {genre} movie is {get_best_movie_type(movies, genre)['Title']} created in {get_best_movie_type(movies, genre)['Year']}")
genre = 'Comedy'
print(f"The best {genre} movie is {get_best_movie_type(movies, genre)['Title']} created in {get_best_movie_type(movies, genre)['Year']}")


# 6. get the list of directors - each list element is one director
def get_directors(movies):
    directors = []
    for movie in movies:
        if ',' in movie['Director']:  # check if provided more than one director
            for director in movie['Director'].split(','):  # iterate for each director separated by comma
                directors.append(director.strip())
        else:
            directors.append(movie['Director'])  # only one director so append directors list
    return directors


print(f'List of all directories: {get_directors(movies)}')
