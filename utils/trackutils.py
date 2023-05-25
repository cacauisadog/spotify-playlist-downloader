def get_song_artists(song) -> str:
    artists: list = []
    for artist in song["track"]["artists"]:
        artists.append(artist["name"])

    return ", ".join(artists)
