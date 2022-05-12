"""
Day 46: Musical Time Machine
"""
# import top_100
import ast
from spotipy.oauth2 import SpotifyOAuth


# Load and save credentials

# Read in credential string and save as a dictionary
with open('../../../Dropbox/100DaysOfCodePRIVATE/Day46Creds.txt') as file:
    creds_str = file.read()
    creds = ast.literal_eval(creds_str)

# Save tokens as variables
SPOTIPY_CLIENT_ID = creds['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = creds['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = 'http://example.com'

auth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)

auth.get_auth_response()

# # Creates a playlist for a user
#
# import argparse
# import logging
#
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
#
# logger = logging.getLogger('examples.create_playlist')
# logging.basicConfig(level='DEBUG')
#
#
# def get_args():
#     parser = argparse.ArgumentParser(description='Creates a playlist for user')
#     parser.add_argument('-p', '--playlist', required=True,
#                         help='Name of Playlist')
#     parser.add_argument('-d', '--description', required=False, default='',
#                         help='Description of Playlist')
#     return parser.parse_args()
#
#
# def main():
#     args = get_args()
#     scope = "playlist-modify-public"
#     sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
#     user_id = sp.me()['id']
#     sp.user_playlist_create(user_id, args.playlist)
#
#
# if __name__ == '__main__':
#     main()
