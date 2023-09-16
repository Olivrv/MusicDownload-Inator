from spotinfo import get_hundred_songs
from tools import download

# max = 100 songs
link = input('Please insert the link of the spotify playlist. ')
offset = int(input("Offset of first song. "))
last_song = (int(input("Limit. ")))
playlist_link = link[-22:]
songs = get_hundred_songs(playlist_link, (last_song - offset), offset)
print("Starting download of: ", *songs)
for i in songs:
    download(i, download_location="La chambre 4")
    print("Downloaded", i)
print("Done.")
