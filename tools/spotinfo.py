import requests

CLIENT_ID = None
CLIENT_SECRET = None
try:
    from config import CLIENT_ID, CLIENT_SECRET
except ModuleNotFoundError:
    print("Error: Set up your Spotify developer account.")

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


def get_hundred_songs(playlist_id: str, limit=100, offset=0) -> list:
    r = requests.get(BASE_URL + 'playlists/' + playlist_id + '/tracks',
                     headers=headers,
                     params={'include_groups': 'track', 'limit': limit, 'offset': offset})

    d = r.json()
    tracks = list()
    for track in d['items']:
        tracks.append(track['track']['name'] + ' by ' + track["track"]["album"]["artists"][0]["name"])
    return tracks


def get_playlist_items(playlist_id: str, limit=50) -> list:
    r = requests.get(BASE_URL + 'playlists/' + playlist_id + '/tracks',
                     headers=headers,
                     params={'include_groups': 'track', 'limit': min(limit, 100)})

    d = r.json()
    tracks = list()
    for track in d['items']:
        tracks.append(track['track']['name'] + ' by ' + track["track"]["album"]["artists"][0]["name"])
    offset = 0
    tracks = list()
    for i in range(int(limit / 100)):
        tracks += (get_hundred_songs(playlist_id, offset=offset))
        offset += 100
    tracks += (get_hundred_songs(playlist_id, limit=(limit % 100), offset=offset))
    return tracks


def get_fifty_songs_album(album_id: str, limit=50, offset=0) -> list:
    r = requests.get(BASE_URL + 'albums/' + album_id + "/tracks", headers=headers,
                     params={'include_groups': 'track', 'limit': limit, 'offset': offset})
    d = r.json()
    tracks = list()
    for track in d['items']:
        tracks.append(track['name'] + ' by ' + track["artists"][0]["name"])
    return tracks


def get_album_items(album_id: str, limit=50) -> list:
    r = requests.get(BASE_URL + 'albums/' + album_id + "/tracks", headers=headers,
                     params={'include_groups': 'track', 'limit': min(limit, 50)})
    d = r.json()
    tracks = list()
    for track in d['items']:
        tracks.append(track['name'] + ' by ' + track["artists"][0]["name"])
    offset = 0
    tracks = list()
    for i in range(int(limit / 50)):
        tracks += (get_fifty_songs_album(album_id, offset=offset))
        offset += 50
    tracks += (get_fifty_songs_album(album_id, limit=(limit % 100), offset=offset))
    return tracks
