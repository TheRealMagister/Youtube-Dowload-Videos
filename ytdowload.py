import os
from pytube import YouTube

def download_video(url):
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    video.download(desktop)
    
while True:
    url = input("Enter the URL of the YouTube video (When the download is complete, a message will appear here, and the file will be available on the desktop): ")
    if url == 'exit':
        break
    download_video(url)
 
print("full download!")
