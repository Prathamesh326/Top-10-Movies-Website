import requests
from pprint import pprint

API_KEY = "76857e0da76e8810a2eefa1eb4c7f9cb"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DETAILS = "https://api.themoviedb.org/3/movie"

response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": API_KEY, "query": "The Matrix"})
id = response.json()['results']
pprint(id)
movie = requests.get(MOVIE_DETAILS, params={"api_key": API_KEY, 'movie_id': id})

pprint(movie.json())
