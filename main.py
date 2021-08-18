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
        download(song, suffix, download_location, quick_mode)
        print("Done.")
    elif choice1 == 2:
        choice2 = int(input("Would you like to download the songs from a list (.txt file) (1)"
                            " or from a playlist (Spotify or Youtube) (2) ? \n>>> "))
        if choice2 == 1:
            inputList = input("Please enter the path to the list.\n>>> ")

        elif choice2 == 2:
            choice3 = int(input("Would you like to download the songs from a Youtube playlist (1) or from a Spotify"
                                " playlist (2) ? \n>>> "))

            if choice3 == 1:
                inputYoutubePlaylist = input("Please enter the link of the playlist.\n>>> ")


            elif choice3 == 2:
                inputSpotifyPlaylist = input("Please enter the link of the playlist.\n>>> ")
                playlist_link = inputSpotifyPlaylist[-22:]
                songs = get_playlist_items(playlist_link)
                print("Starting download of: ", *songs)
                for i in songs:
                    download(i)
                    print("Downloaded", i)
                print("Done.")

            else:
                print("Error: please input either 1 or 2.")
        else:
            print("Error: please input either 1 or 2.")
    else:
        print("Error: please input either 1 or 2.")


if __name__ == "__main__":
    main()
