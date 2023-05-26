import os

from utils.dataclasses import Song
from utils.spoti import get_songs_from_playlist
from utils.trackutils import get_song_artists

if __name__ == "__main__":
    playlist_id = "4pGq7Lgh8cilEk2wCX6Hkp"
    songs = get_songs_from_playlist(playlist_id)
    song_list: list[Song] = []
    for song in songs["tracks"]["items"]:
        artist = get_song_artists(song)
        name = song["track"]["name"]
        song_list.append(Song(artist, name))

    for song in song_list:
        os.system(f"youtube-dl -x --audio-format mp3 'ytsearch1:{song.track()}'")
