from spotinfo import get_playlist_items, get_hundred_songs
from tools import download


link = input('Please insert the link of the spotify playlist. ')
offset = int(input("Offset of first song. "))
lastsong= (int(input("Limit. ")))
playlist_link = link[-22:]
songs = get_hundred_songs(playlist_link, (lastsong - offset), offset)
print("Starting download of: ", *songs)
for i in songs:
    download(i)
    print("Downloaded", i)
print("Done.")
