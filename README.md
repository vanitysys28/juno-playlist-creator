# Junodownload Playlist Creator

junodownload is a great website for finding new releases for different electronic music genres.    
Many songs found there can also be found on Spotify.

This tool is gathering all releases in the previous 8 weeks, and adding them automatically in a specified Spotify playlist.

## Spotify API Limitations

The Spotify client is notifying whenever we attempt to add a song already in a playlist.    
The API isn't currently offering any direct mean to check for possible duplicates. 

For this reason, the script needs to keep log of all previously scraped songs, and check all past logs for duplicates.