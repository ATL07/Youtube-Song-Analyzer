import yt_dlp

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'data/song.%(ext)s',  # saves in data/ folder
        'ffmpeg_location': r'C:\Users\aymen\Desktop\youtube-song-analyzer\ffmpeg-2026-03-15-git-6ba0b59d8b-essentials_build\bin',
        'noplaylist': True,  # ensures only 1 video is downloaded
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',  # converts audio to .wav
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print("⬇️ Downloading audio...")
            ydl.download([url])
            print("✅ Download complete!")
        except Exception as e:
            print(f"❌ Error downloading audio: {e}")