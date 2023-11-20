from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# url = "https://www.junodownload.com/drumandbass/eight-weeks/releases/?items_per_page=100"

# r = requests.get(url = URL)
# soup = BeautifulSoup(r.text, features="html.parser")

# duplicate = []
# new = []

# print("Script starting")

# while len(soup.find_all("a",{"title":"Next Page"})) > 0:
#     r = requests.get(url = URL)
#     soup = BeautifulSoup(r.text, features="html.parser")
#     file = open("drumoandbasso.txt","a",encoding="utf-8")
    
#     for data in soup.find_all("div", {"class":"col-12 col-md order-4 order-md-3 mt-3 mt-md-0 pl-0 pl-md-2"}):
#         line = data("div", {"class":"col juno-artist"})[0].get_text().replace("/", " ") + "    " + data("a", {"class":"juno-title"})[0].get_text()

#         with open('drumoandbasso.txt') as f:
#             if line in f.read():
#                 duplicate.append(line)
#             else:
#                 file.write(data("div", {"class":"col juno-artist"})[0].get_text().replace("/", ", ") + "    " + data("a", {"class":"juno-title"})[0].get_text())
#                 file.write('\n')
#                 new.append(line)

#     if len(soup.find_all("a",{"title":"Next Page"})) > 0:
#         URL = soup.find("a",{"title":"Next Page"})['href']

# print(str(len(duplicate)) + " items already in song list")
# print(str(len(new)) + " songs added to song list")




# scope = "playlist-modify-private,playlist-modify-public"

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri="http://localhost:8888/callback",scope=scope))


# file = open("drumoandbasso.txt",encoding="utf-8")
# lines = file.readlines()
# for line in lines:
#     try:
#         albumid = sp.search(q=line, limit=20,type='track')['tracks']['items'][0]['album']['id']
#         try:
#             albumtracks = sp.album_tracks(albumid)['items']
#             for tracks in albumtracks:
#                 print(tracks['uri'])
#                 playlistadd = sp.playlist_add_items(PLAYLIST_ID,[tracks['uri']],position=None)
#         except:
#             print("No match while searching for track")
#     except:
#         print('No match while searching for ' + line)
    