import json


with open('movies.json') as f:  # open json file
    movies = json.load(f)  # create object movies which is the list of movies

# movie object structure
# {'Title': 'The Shawshank Redemption',
#  'Year': 1994,
#  'Genre': 'Crime, Drama',
#  'Director': 'Frank Darabont',
#  'Writer': 'Stephen King, Frank Darabont',
#  'imdbRating': 9.3,
#  'imdbVotes': 1078045}

# 6. get the list of directors - each list element is one director
# 7. get the list of unique directors - each list element is one director
# 8. get the dict with occurences count in db for each director


# 6. get the list of directors - each list element is one director
def get_directors(movies):
    directors = []
    for movie in movies:
        if ',' in movie['Director']:  # check if comma found - if yes movie was directed by more than one director
            temporary_directors = movie['Director'].split(', ')  # split directors names
            for director in temporary_directors:
                directors.append(director)
        else:
            directors.append(movie["Director"])
    return directors


print(f'List of all directories: {get_directors(movies)}')


# 7. get the list of unique directors - each list element is one director
def get_unique_directors(movies):
    directors = []
    for movie in movies:

        if movie['Director'] not in directors:  # ensure that director names was not included in directors list

            if ',' in movie['Director']:
                temporary_directors = movie['Director'].split(', ')
                for director in temporary_directors:
                    if director not in directors:
                        directors.append(director)
            else:
                directors.append(movie["Director"])
    return directors


print(f'List of all unique directories: {get_unique_directors(movies)}')


# 8. get the dict with occurences count in db for each director
def get_occurences(movies):
    directors = get_directors(movies)
    occurences = {}
    for director in directors:
        if director in occurences:
            occurences[director] += 1
        else:
            occurences[director] = 1
    return occurences


print(f'How many movies was directed by particular director: {get_occurences(movies)}')
