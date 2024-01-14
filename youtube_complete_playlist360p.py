from pytube import Playlist, YouTube
from tqdm import tqdm
import os

def download_playlist(playlist_url, resolution='360p'):
    try:
        # Create a Playlist object
        playlist = Playlist(playlist_url)

        # Set the download path to the 'Downloads' folder
        download_path = os.path.join(os.path.expanduser('~'), 'Downloads', playlist.title)

        # Create the download directory if it doesn't exist
        os.makedirs(download_path, exist_ok=True)

        for video_url in tqdm(playlist.video_urls, desc=f"Downloading Playlist '{playlist.title}'"):
            # Create a YouTube object for each video in the playlist
            yt_video = YouTube(video_url)

            # Get the stream with the specified resolution
            video_stream = yt_video.streams.filter(res=resolution, file_extension='mp4').first()

            # Download the video to the download path
            video_file_path = os.path.join(download_path, f"{yt_video.title}.mp4")
            video_stream.download(download_path)

        print(f"\nPlaylist downloaded successfully to {download_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Prompt the user for a YouTube playlist link
    playlist_url = input("Enter the YouTube playlist link: ")

    # Download the entire playlist in 360p resolution
    download_playlist(playlist_url, resolution='360p')
