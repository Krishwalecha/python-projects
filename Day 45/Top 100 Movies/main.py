import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

movie_list = soup.find_all("h2")

# Extract movie titles in reverse order, skipping first 3 non-movie headers
movie_titles = [h2.getText().strip() for h2 in movie_list[-1:2:-1]]

with open('movies.txt', "w") as file:
    for movie in movie_titles:
        file.write(movie + "\n")
