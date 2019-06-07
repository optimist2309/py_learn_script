"""
Python script to get the IMDB_RATING, IMDB_VOTES, Relese_Date , Movie_Genre, , Metacritics_score using omdbapi.

The OMDb API is a RESTful web service to obtain movie information, all content and images on the site are contributed and maintained by our users.

The OMDb API is free for 1000 daily calls.

To claim your api key visit this link 'http://www.omdbapi.com/apikey.aspx'
 
"""

import requests

movie_name = raw_input('Enter the movie name : ')

req_api_url = "http://www.omdbapi.com/?"+"t"+"="+movie_name+"&apikey=yourapikey"

movie_name_request = requests.get(req_api_url)
movie_data = movie_name_request.json()

if movie_data['Response'] == 'False':
    print("Movie is not available in api database.")
else:
    print("Imdb rating for the movie is " + movie_data['imdbRating'] + ".")
    print("Total Number of the imdb votes is " + movie_data['imdbVotes']+ ".")
    print("Release date of the movie is " + movie_data['Released']+ ".")
    print("Genre of the movie is " + movie_data['Genre']+ ".")
    print("Metacritic score for the movie is " + movie_data['Metascore']+ ".")
        