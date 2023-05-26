import os
import re
import sys

from utils.dataclasses import Song
from utils.spoti import get_songs_from_playlist
from utils.trackutils import get_song_artists

if __name__ == "__main__":
    playlist_url = sys.argv[1]
    pattern = r"\/playlist\/([A-Za-z0-9]+)"
    match = re.search(pattern, playlist_url)
    if not match:
        raise "Not a valid Spotify playlist url."

    playlist_id = match.group(1)
    songs = get_songs_from_playlist(playlist_id)
    song_list: list[Song] = []
    for song in songs["tracks"]["items"]:
        artist = get_song_artists(song)
        name = song["track"]["name"]
        song_list.append(Song(artist, name))

    for song in song_list:
        os.system(f"youtube-dl -x --audio-format mp3 -o './songs/%(title)s.%(ext)s' 'ytsearch1:{song.track()}'")
