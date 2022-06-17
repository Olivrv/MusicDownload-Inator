from spotinfo import get_fifty_songs_album
from tools import download

link = input('Please insert the link of the spotify album. ')
offset = int(input("Offset of first song. "))
last_song = (int(input("Limit. ")))
loc = input("Download to: ")
album_link = link[-22:]
songs = get_fifty_songs_album(album_link, (last_song - offset), offset)
print("Starting download of: ", *songs)
for i in songs:
    download(i, download_location=loc)
    print("Downloaded", i)
print("Done.")
