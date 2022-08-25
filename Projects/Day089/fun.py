"""
Helper functions
"""
import datetime

timestamp = datetime.datetime.now().strftime('%Y.%m.%d-%H.%M')
text_file = open(f"../../../Downloads/writing_session_{timestamp}.txt", "w")
text_file.write('Jello World')