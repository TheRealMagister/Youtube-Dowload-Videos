import os
from pytube import YouTube

def download_video(url):
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    video.download(desktop)

url = input("Insira a URL do vídeo do YouTube (Quando o dowload estiver completo ira aparecer uma mensagem aqui, e o arquivo estara disponivel na area de trabalho): ")
download_video(url)
print("dowload completo!")