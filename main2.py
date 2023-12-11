import requests

MOVIE_DB_API_KEY = "16395cddf1e4c80579f6f1dcd380baed"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"  # Correct endpoint for movie search

# Parameters for the movie search API
params = {
    "api_key": MOVIE_DB_API_KEY,
    "query": "Old"  # Replace "Old" with the desired search term
}

# Make a GET request to search for movies
response = requests.get(MOVIE_DB_SEARCH_URL, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()["results"]
    print(data)
else:
    print("Failed to fetch data. Status code:", response.status_code)
