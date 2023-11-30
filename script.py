import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def scrapeJuno():
    url = "https://www.junodownload.com/drumandbass/eight-weeks/releases/?items_per_page=100"
    soup = BeautifulSoup(requests.get(url).text, features="html.parser")

    while len(soup.find_all("a",{"title":"Next Page"})) > 0:
        soup = BeautifulSoup(requests.get(url).text, features="html.parser")
        file = open("data.txt","a",encoding="utf-8")
                
        for data in soup.find_all("div", {"class":"col-12 col-md order-4 order-md-3 mt-3 mt-md-0 pl-0 pl-md-2"}):
            entry = data("div", {"class":"col juno-artist"})[0].get_text().replace("/", " ") + "    " + data("a", {"class":"juno-title"})[0].get_text()

            with open('data.txt') as f:
                if entry not in f.read():
                    file.write(entry)
                    file.write('\n')

        if len(soup.find_all("a",{"title":"Next Page"})) > 0:
            url = soup.find("a",{"title":"Next Page"})['href']

def addToSpotifyPlaylist():
    load_dotenv()

    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    playlist_id = os.getenv('PLAYLIST_ID')

    scope = "playlist-modify-private,playlist-modify-public"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,client_secret,redirect_uri="http://localhost:8888/callback",scope=scope))

    file = open("data.txt",encoding="utf-8")
    lines = file.readlines()
    for line in lines:
            albumid = sp.search(q=line, limit=20,type='track')['tracks']['items'][0]['album']['id']
            albumtracks = sp.album_tracks(albumid)['items']
            for tracks in albumtracks:
                playlistadd = sp.playlist_add_items(playlist_id,[tracks['uri']],position=None)
    
def main():
    scrapeJuno()
    addToSpotifyPlaylist()

if __name__ == "__main__":
    main()