import datetime
import os
import requests
import spotipy
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

def createDataFolder():
    if os.path.exists('data/') != True:
        os.mkdir('data/')

def readFilesInDataFolder():
    filecontents = ''

    for files in os.listdir('data/'):
        with open('data/' + files) as f:
            filecontents += f.read()

    scrapeJuno(filecontents, genreSelector(), timeLapseSelector())

def genreSelector():
    selection = input('''
    Select genre by typing associated number:

    1 - Drum and Bass
    2 - Hard Techno
    3 - Trance

    Your selection: ''')

    if selection == '1':
        return 'drumandbass'
    if selection == '2':
        return 'hard-techno'
    if selection == '3':
        return 'trance-music'

def timeLapseSelector():
    selection = input('''
    Select time lapse by typing associated number:

    1 - Last Week
    2 - Last 2 Weeks
    3 - Last 4 Weeks
    4 - Last 8 Weeks

    Your selection: ''')

    if selection == '1':
        return 'this-week'
    if selection == '2':
        return 'two-weeks'
    if selection == 3:
        return 'four-weeks'
    if selection == '4':
        return 'eight-weeks'
    
def scrapeJuno(filecontents, genre, timelapse):
    url = 'https://www.junodownload.com/' + genre + '/' + timelapse + '/releases/?items_per_page=100'
    soup = BeautifulSoup(requests.get(url).text, features='html.parser')

    while len(soup.find_all('a',{'title':'Next Page'})) > 0:
        soup = BeautifulSoup(requests.get(url).text, features='html.parser')
        file = open('data/' + now + '.txt','a',encoding='utf-8')
        
        for data in soup.find_all('div', {'class':'col-12 col-md order-4 order-md-3 mt-3 mt-md-0 pl-0 pl-md-2'}):
            entry = data('a', {'class':'juno-title'})[0].get_text() + ' label:' + data('a', {'class':'juno-label'})[0].get_text().split()[0]

            with open('data/' + now + '.txt'):
                if entry not in filecontents:
                    file.write(entry)
                    file.write('\n')

        if len(soup.find_all('a',{'title':'Next Page'})) > 0:
            url = soup.find('a',{'title':'Next Page'})['href']

def addToSpotifyPlaylist():
    load_dotenv()

    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    playlist_id = os.getenv('PLAYLIST_ID')

    scope = 'playlist-modify-private,playlist-modify-public'

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,client_secret,redirect_uri='http://localhost:8888/callback',scope=scope))

    file = open('data/' + now + '.txt',encoding='utf-8')
    lines = file.readlines()
    for line in lines:
        if sp.search(q=line, limit=20,type='track')['tracks']['items']:
            albumid = sp.search(q=line, limit=20,type='track')['tracks']['items'][0]['album']['id']
            albumtracks = sp.album_tracks(albumid)['items']
            for tracks in albumtracks:
                playlistadd = sp.playlist_add_items(playlist_id,[tracks['uri']],position=None)
    
def main():
    createDataFolder()
    readFilesInDataFolder()
    addToSpotifyPlaylist()
    
if __name__ == '__main__':
    main()
