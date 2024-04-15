from pytube import YouTube
from pytube.innertube import _default_clients

_default_clients["ANDROID_MUSIC"] = _default_clients["WEB"]

#downloads youtube video as mp4
def download(link):
    youtube_object = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    youtube_video = youtube_object.streams.get_highest_resolution()
    try:
        youtube_video.download()
        print("Download completed successfully.")
    except:
        print("An error has occured.")

link = input("Enter the youtube URL here : ")
download(link)
