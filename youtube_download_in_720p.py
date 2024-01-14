from pytube import YouTube
from tqdm import tqdm
import os

def download_youtube_video(url, resolution='720p'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream with both video and audio
        video_stream = yt.streams.filter(res=f'{resolution}').first()

        # Set the download path to the 'Videos' folder
        download_path = os.path.join(os.path.expanduser('~'), 'Videos')

        # Download the video with a progress bar
        with tqdm(total=video_stream.filesize, unit='B', unit_scale=True, desc="Downloading") as progress_bar:
            video_stream.download(download_path, on_progress_callback=lambda stream, chunk, file_handle, bytes_remaining: progress_bar.update(chunk))

        print(f"\nVideo downloaded successfully to {download_path}")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Prompt the user for a YouTube link
    youtube_link = input("Enter the YouTube video link: ")

    # Download the video in 720p with audio
    download_youtube_video(youtube_link)
