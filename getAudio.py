import yt_dlp

options = {
    'format': 'bestaudio/best',
    'outtmpl': 'tmp/output',
    'keepvideo': False,
    'nooverwrites': False,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '0'
    }],
}

def youtube_download(video_url):
    yt_dlp.YoutubeDL(options).download([video_url])

if __name__ == "__main__":
    url = input("Enter the URL of the YouTube video: ")
    youtube_download(url)