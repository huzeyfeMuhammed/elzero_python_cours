from pytube import Playlist,YouTube

playlist_url = input('Playlist URL : ')

pl = Playlist(playlist_url)
# pl.playlist_url()

i=0
print('Starting...')
for video_url in pl.video_urls:
    i = i + 1
    try:
        yt = YouTube(video_url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video.download(f"Videos/{yt.author}")
        print(f"Done !! {i} / {len(pl.video_urls)}")
    except:
        print(f"Feld to download !! {i} / {len(pl.video_urls)}")
        continue
    
print('ALL DONE ')