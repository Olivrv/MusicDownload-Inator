import requests
from config import CLIENT_ID, CLIENT_SECRET

BASE_URL = 'https://api.spotify.com/v1/'

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}


def get_playlist_items(playlist_id: str, limit=50) -> list:
    r = requests.get(BASE_URL + 'playlists/' + playlist_id + '/tracks',
                     headers=headers,
                     params={'include_groups': 'track', 'limit': limit})

    d = r.json()
    tracks = list()
    for track in d['items']:
        tracks.append(track['track']['name'] + ' by ' + track["track"]["album"]["artists"][0]["name"])
    return tracks
