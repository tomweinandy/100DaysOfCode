"""
Day 46: Musical Time Machine
"""
from top_100 import input_date
import ast
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Read in credential string and save as a dictionary
with open('../../../Dropbox/100DaysOfCodePRIVATE/Day46Creds.txt') as file:
    creds_str = file.read()
    creds = ast.literal_eval(creds_str)

# Save tokens as variables
SPOTIPY_CLIENT_ID = creds['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = creds['SPOTIPY_CLIENT_SECRET']

auth = SpotifyOAuth(
    scope='playlist-modify-public',
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri='http://example.com',
    show_dialog=True
)

sp = spotipy.Spotify(auth_manager=auth)

print(sp.current_user()['id'])
print(input_date)

# Creates a playlist for a user
playlist = sp.user_playlist_create(
                user=sp.current_user()['id'],
                name=f'Top100--{input_date}',
                description=f'Top 100 Songs (if available) from {input_date}.'
            )

# todo Troubleshoot Step 3 from here
