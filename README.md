# Python source files for extracting mp4s

youtube.py grabs video from youtube.com provided with the URL of the video.

mp4.py grabs an embedded webcast via https request.


## notes

bug in pytube module. change _default_clients = "WEB" is slow but always works; depending on the browser or operating system, this may also be solved using _default_clients = "ANDROID_MUSIC", "ANDROID_CREATOR", "IOS", etc..
