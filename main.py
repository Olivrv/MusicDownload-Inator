from os import path
import sys
from os import rename

from moviepy.editor import *
from pytube import YouTube
from youtube_search import YoutubeSearch as yts

SUFFIX = "audio"


Download_loc = sys.argv[0].strip("main.py")


def get_urls(titles: list, suffix="audio"):
    """
    :param titles: List of music titles to download
    :param suffix: Optional, word added at the end of the query (default: audio)
    :return: Dictionary linking music titles (input) to their youtube urls
    """
    urls = {}
    for i in titles:
        search = yts(i + suffix, max_results=1).to_dict()
        name = search[0]['title']
        url = "https://www.youtube.com" + search[0]['url_suffix']
        urls[name] = url
    return urls


def download_from_url(url: str, download_path="Downloads"):
    """
    :param quick: Boolean, choose if the download will be  long or quick. Quick will result in a quick convert, and an
    unreadable file by Itunes and most programs
    :param url: Youtube urls of musics to download
    :param download_path: Optional path where to download the music file
    :return: Downloads the music, and returns absolute path of the downloaded music
    """
    vid = YouTube(url)
    stream = vid.streams.filter().first()
    outputPath = stream.download(output_path=download_path)
    return outputPath


def download_from_name(name, suffix="audio", download_path="Downloads"):
    """
    :param name: Name of the music to download
    :return: Downloads the music, and returns absolute path of the downloaded music
    """
    search = yts(name + suffix, max_results=1).to_dict()
    link = "https://www.youtube.com" + search[0]['url_suffix']
    return download_from_url(link, download_path)


def quick_convert(file):
    """
    :param file: Absolute path to the file to convert
    :return: None, but converts the file to mp3
    """
    name, ext = path.splitext(file)
    rename(file, name + ".wma")


def long_convert(file):
    mp3_file = file.strip(".mp4") + ".mp3"
    video_clip = VideoFileClip(file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(mp3_file, verbose=False, logger=None)
    audio_clip.close()
    video_clip.close()
    os.remove(file)


def download(name, suffix="audio", download_location="Downloads", quick=False):
    file = download_from_name(name, suffix, download_location)
    song_name, ext = path.splitext(file)
    str_strip = Download_loc + "/" + download_location
    song_name = song_name.strip(str_strip)
    if quick:
        quick_convert(file)
    else:
        long_convert(file)
    return song_name


def main(name=str(sys.argv), suffix="audio", download_location=sys.argv[0].strip("main.py") + "/Downloads",
         quick_mode=False):

    print(download(name, suffix, download_location, quick_mode))


if __name__ == "__main__":
    main()