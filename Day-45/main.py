from importlib.metadata import files

from bs4 import BeautifulSoup
import requests

url = 'https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# Find all elements with the specific class
movie_container = soup.find_all('h2')

movie_titles = [movie.getText() for movie in movie_container]
movies       = movie_titles[::-1]

with open('movie.txt' , mode='w') as f:
    for movie in movies:
        f.write(f'{movie}\n')
