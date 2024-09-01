import yt_dlp

options = {
    'format': 'bestaudio/best',
    'outtmpl': 'tmp/output.mp3',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '0',
    }],
}

def youtube_download(video_url):
    yt_dlp.YoutubeDL(options).download([video_url])