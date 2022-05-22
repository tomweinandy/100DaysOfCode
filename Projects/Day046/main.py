"""
Day 46: Musical Time Machine
"""
from top_100 import input_date, df
import ast
import spotipy
from spotipy.oauth2 import SpotifyOAuth

print('Scraped Billboard Top 100 songs from given date.')

# Read in credential string and save as a dictionary
with open('../../../../Dropbox/100DaysOfCodePRIVATE/Day46Creds.txt') as file:
    creds_str = file.read()
    creds = ast.literal_eval(creds_str)

# Save tokens as variables
SPOTIPY_CLIENT_ID = creds['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = creds['SPOTIPY_CLIENT_SECRET']

# Load authorization and initialize spotipy class
auth = SpotifyOAuth(
    scope='playlist-modify-public',
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri='http://example.com',
    show_dialog=True
)
sp = spotipy.Spotify(auth_manager=auth)
user_id = sp.current_user()['id']

# Creates a playlist for a user
playlist = sp.user_playlist_create(
                user=sp.current_user()['id'],
                name=f'Top 100 from {input_date}',
                description=f'Top 100 Songs (if available) from {input_date}.'
            )

print('Created empty playlist.')
print('Searching for Top 100 songs on Spotify...')

# Add songs to playlist
playlist_id = playlist['id']
track_list = []

for idx in df.index:
    row = df.iloc[idx]
    song_artist = f"{row['Song']}, {row['Artist']}"

    query = sp.search(song_artist, limit=1)

    try:
        track_id = query['tracks']['items'][0]['id']
        track_list.append(track_id)
    except IndexError:
        print(f'Cannot find {song_artist}')

sp.playlist_add_items(playlist_id=playlist_id, items=track_list)

print('Finished. See Spotify for 100-song playlist.')