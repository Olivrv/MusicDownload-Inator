from spotinfo import get_playlist_items
from tools import *


link = input('Please insert the link of the spotify playlist.')
# link = "https://open.spotify.com/playlist/1qGJ2P1ajUosy5PFAlMqTr"
playlist_link = link[-22:]
songs = get_playlist_items(playlist_link)
print("Starting download of: ", *songs)
for i in songs:
    download(i)
    print("Downloaded", i)
print("Done.")
