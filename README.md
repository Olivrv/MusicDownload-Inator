# MusicDownload-Inator

<!-- DOWNLOAD MUSIC -->
## Download music in various ways:
* Single mode: input a single music name to be downloaded
* List mode: Input the path of a list written as such :
```#list.txt
song1 author1
song2 author2
song3
```
* Youtube Playlist mode: input a playlist link (playlist must be public or unlisted) for all its songs to be downloaded
* Spotify Playlist mode: input a playlist link (requires a Spotify developer account and credentials) for all its songs to be downloaded

## Custom settings:
There are a few settings you can tweak to your liking:
* `suffix`: The program will search Youtube with your input (single mode or list mode), and append to that search this suffix. (Default = "audio")
* `download_location`: The path where all the songs will be downloaded (all modes). (Default = "Downloads")
* `quick_mode`: A quicker mode to download, but metadata will be lost and the file might be unreadable by some programs, such as Itunes (Default = False)

## Setting up Spotify:
1. Set up your developer account here: 
2. Get your credentials here:
3. Create a config.py file in the project directory as such:
```#config.py
CLIENT_ID = "XXXXXXXXXXXXXXXXXXXXXXX"
CLIENT_SECRET = "XXXXXXXXXXXXXXXXXXXXX"
```
and fill in your credentials.
You can now use the Spotify Playlist mode !


Thank you for using MusicDownload-Inator !
