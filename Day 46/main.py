import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from os import environ
from dotenv import load_dotenv

load_dotenv()

date = input("Which year do you want to travel to? Enter the date in YYYY-MM-DD format: ")

BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date}"
SPOTIPY_CLIENT_ID = environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = "https://example.com/callback"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

response = requests.get(BILLBOARD_URL, headers=headers)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")
song_title_elements = soup.select("li ul li h3")
song_titles = [title.getText().strip() for title in song_title_elements]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private user-read-private",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        show_dialog=True
    )
)

user = sp.current_user()
user_id = user["id"]
print(f"Successfully logged in as {user['display_name']}.")

song_uris = []
year = date.split("-")[0]

# Create a new playlist
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"Billboard Top 100 — {date}",
    public=False,
    description=f"A nostalgic trip to the Billboard Hot 100 on {date}. Relive the biggest chart-toppers of the year!"
)

for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        sp.playlist_add_items(playlist_id=playlist["id"], items=[uri])
    except IndexError:
        print(f"⚠️ '{song}' not found on Spotify. Skipping...")
    else:
        print(f"✅ Added: '{song}'")

print("\n🎵 Your Billboard Time Machine playlist is ready! Check it out on your Spotify account.")
