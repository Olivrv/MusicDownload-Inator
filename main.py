from tools import *
from spotinfo import get_playlist_items


def main(name=str(sys.argv), suffix="audio", download_location="Downloads",
         quick_mode=False):
    print(download(name, suffix, download_location, quick_mode))


def main(suffix="audio", download_location="Downloads", quick_mode=False):
    print(
        """
  __  __           _      _____                      _                 _      _____             _             
 |  \/  |         (_)    |  __ \                    | |               | |    |_   _|           | |            
 | \  / |_   _ ___ _  ___| |  | | _____      ___ __ | | ___   __ _  __| |______| |  _ __   __ _| |_ ___  _ __ 
 | |\/| | | | / __| |/ __| |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |______| | | '_ \ / _` | __/ _ \| '__|
 | |  | | |_| \__ \ | (__| |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |     _| |_| | | | (_| | || (_) | |   
 |_|  |_|\__,_|___/_|\___|_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|    |_____|_| |_|\__,_|\__\___/|_|   
                                                                                                              
 by Olivrv, using moviepy, pytube, requests.
 To download from Spotify you'll need a private CLIENT_ID and CLIENT_SECRET, which you can get from your dev account.                                                                                                       
    """)
    print("Setting up...")
    settings = input("Would you like to apple the recommended settings? (y/n)\n>>> ")
    if settings == 'n':
        suffix = input("New suffix: ")
        download_location = input('Download path: ')
        quick_mode = bool(input("Quick mode (bool): "))
    choice1 = int(input("Would you like to download a single song (1) or multiple songs (2) ? \n>>> "))
    if choice1 == 1:
        song = input('Please enter the name of the song. \n>>> ')
        print("Starting download...")
        name = download(song, suffix, download_location, quick_mode)
        print("Downloaded", name)
        print("Done.")
        input("Press enter to quit.")
    elif choice1 == 2:
        choice2 = int(input("Would you like to download the songs from a list (.txt file) (1)"
                            " or from a playlist (Spotify or Youtube) (2) ? \n>>> "))
        if choice2 == 1:
            inputList = input("Please enter the path to the list (1 song name per line, no commas).\n>>> ")
            try:
                with open(inputList, "r") as f:
                    songs = f.readlines()
                f.close()
                print("Starting download...")
                for i in songs:
                    name = download(i, suffix, download_location, quick_mode)
                    print("Downloaded", name)
                print("Done.")
                input("Press enter to quit.")
            except FileNotFoundError:
                print("Error: Incorrect filename.")

        elif choice2 == 2:
            choice3 = int(input("Would you like to download the songs from a Youtube playlist (1) or from a Spotify"
                                " playlist (2) ? \n>>> "))

            if choice3 == 1:
                inputYoutubePlaylist = input("Please enter the link of the playlist. "
                                             "(Playlist must be public or unlisted)\n>>> ")
                print("Starting download...")
                done = download_from_yt_playlist(inputYoutubePlaylist, download_location, quick_mode)
                if done:
                    print("Done")
                    input("Press enter to quit.")
                else:
                    print("Error: Incorrect playlist link.")

            elif choice3 == 2:
                try:
                    inputSpotifyPlaylist = input("Please enter the link of the playlist.\n>>> ")
                    playlist_link = inputSpotifyPlaylist[-22:]
                    songs = get_playlist_items(playlist_link)
                    print("Starting download...")
                    for i in songs:
                        download(i)
                        print("Downloaded", i)
                    print("Done.")
                    input("Press enter to quit.")
                except KeyError:
                    print("Error: incorrect playlist. (Expected: https://open.spotify.com/playlist/XXXXXXXXXXXX)")

            else:
                print("Error: please input either 1 or 2.")
        else:
            print("Error: please input either 1 or 2.")
    else:
        print("Error: please input either 1 or 2.")


if __name__ == "__main__":
    main()
