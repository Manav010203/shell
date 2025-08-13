# import requests

# def fetch_platlist_songs(playlist_url):
#     if playlist_url.startswith('http://') or playlist_url.startswith('https://'):

#         #dowmload the playlist from the internet
#         response = requests.get(playlist_url)
#         response.raise_for_status() #stop it if HTTp erro
#         content = response.text
#     else:
#         with open(playlist_url,'r') as f:
#             content = f.read()
    

#     songs = [
#         line.strip()
#         for line in content.splitlines()
#         if line.strip() and not line.startswith('#')
#     ]
#     return songs


# import subprocess
# import tempfile
# import os

# def play_song(song_path):
# ## update to song name
#     print(f"Playing: {song_path}")

#     if song_path.startswith('http://') or song_path.startswith('https://'):
#         with tempfile.NamedTemporaryFile(suffix='.mp3',delete=False) as tmp_file:
#             print(f"Downloading from {song_path}...")
#             resp = requests.get(song_path,stream=True)
#             resp.raise_for_status()
#             for chunk in resp.iter_content(chunk_size=8192):
#                 tmp_file.write(chunk)
#             tmp_filename = tmp_file.name
#         subprocess.run(['afplay',tmp_filename])
#         os.remove(tmp_filename)
#     else:
#         subprocess.run(['afplay',song_path])


# def play_platlist(playlist_link):

#     try:
#         songs = fetch_platlist_songs(playlist_link)

#         if not songs:
#             print("NO VALID SONGS FOUND IN THE PLAYLIST")
#             return
        
#         for song in songs:
#             play_song(song)

#         print("Finished playing playlist....")
#     except Exception as e:
#         print(f"Error: {e}")


# if __name__=="__main__":
#     playlist_link = input("ENTER THE PLAYLIST LINK YOU WANT TO PLAY: ").strip()
#     play_platlist(playlist_link)


import subprocess

def fetch_youtube_audio_urls(playlist_url):
    result = subprocess.run(
        ["yt-dlp", "-f", "bestaudio", "--get-url", playlist_url],
        capture_output=True, text=True, check=True
    )
    return result.stdout.strip().split("\n")

def play_song(song_url):
    print(f"🎵 Now playing: {song_url}")
    subprocess.run(["mpv", "--no-video", song_url])

def play_playlist(playlist_url):
    try:
        songs = fetch_youtube_audio_urls(playlist_url)
        if not songs:
            print("⚠️ No audio streams found.")
            return
        for song in songs:
            play_song(song)
        print("✅ Finished playing playlist.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    playlist_link = input("Enter YouTube playlist link: ").strip()
    play_playlist(playlist_link)
