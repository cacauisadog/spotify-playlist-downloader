import spotipy
from dotenv.main import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_songs_from_playlist(playlist_id: str) -> dict:
    results = sp.playlist(playlist_id)
    return results
