import requests

CLIENT_ID = "e0ad36f1d50c48d5947d88e78c359678"
CLIENT_SECRET = "18ad5486606a4394a7a9b23d2da8450b"
BASE_URL = 'https://api.spotify.com/v1/'
PLAYLIST_ID = ""

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


def get_playlist_items(playlist_id):
    r = requests.get(BASE_URL + 'playlists/' + playlist_id + '/tracks',
                     headers=headers,
                     params={'include_groups': 'track', 'limit': 50})

    d = r.json()
    tracks = list()
    for track in d['items']:
        tracks.append(track['track']['name'] + ' by ' + track["track"]["album"]["artists"][0]["name"])
    return tracks


def main():
    r = requests.get(BASE_URL + 'playlists/' + PLAYLIST_ID + '/tracks',
                     headers=headers,
                     params={'include_groups': 'track', 'limit': 50})

    d = r.json()

    for track in d['items']:
        print(track['track']['name'] + ' by ' + track["track"]["album"]["artists"][0]["name"])


if __name__ == "__main__":
    main()


