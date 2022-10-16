"""
Day 90: PDF to Audiobook Converter

AWS speech-to-text API Polly: https://aws.amazon.com/polly/
"""
import time
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir
import json
import PyPDF2
from mutagen.mp3 import MP3

# Read credentials file saved locally
with open('../../../../Dropbox/100DaysOfCodePRIVATE/Day90Creds.json') as file:
    creds = json.loads(file.read())

# Define credentials as read credentials file
ACCESS_KEY = creds['access_key']
SECRET_KEY = creds['secret_key']
REGION = 'us-east-1'

# Create session with creds
session = Session(aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY,
                  region_name=REGION)
polly = session.client("polly")

# Read sample file
filename = 'sample_input.pdf'
pdfFileObj = open(filename, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Initialize string for storing pdf text
text = ''

# Loop though each page of pdf (helps prevent hitting API limits)
for i in range(pdfReader.numPages):
    # Extract text from the i-th page and add it to the text string
    page_obj = pdfReader.getPage(i)
    page_text = page_obj.extractText()
    text += page_text
    text += ' \n '

    try:
        # Make an API call to covert the text to speech
        response = polly.synthesize_speech(Text=page_text, OutputFormat="mp3", VoiceId="Joanna")
    except (BotoCoreError, ClientError) as error:
        # The service returned an error, exit gracefully
        print(error)
        sys.exit(-1)

    # Access the audio stream from the response
    if "AudioStream" in response:
        # Note: Closing the stream is important because the service throttles on the
        # number of parallel connections. Here we are using contextlib.closing to
        # ensure the close method of the stream object will be called automatically
        # at the end of the with statement's scope.
        with closing(response["AudioStream"]) as stream:
            output = f"../../../../Downloads/speech_page{i+1}.mp3"

            try:
                # Open a file for writing the output as a binary stream
                with open(output, "wb") as file:
                    file.write(stream.read())

                    # Get audio length
                    audio_file = MP3("../../../../Downloads/speech_page1.mp3")
                    audio_length = audio_file.info.length

            # If filepath to downloads folder not correct, try saving to current working directory
            except FileNotFoundError as error:
                print(error)

                try:
                    output = f"speech{i+1}.mp3"
                    with open(output, "wb") as file:
                        file.write(stream.read())
                except IOError as error:
                    # Could not write to file, exit gracefully
                    print(error)
                    sys.exit(-1)

            except IOError as error:
                # Could not write to file, exit gracefully
                print(error)
                sys.exit(-1)

    else:
        # The response didn't contain audio data, exit gracefully
        print("Could not stream audio")
        sys.exit(-1)

    # Play the audio using the platform's default player
    if sys.platform == "win32":
        os.startfile(output)
    else:
        # The following works on macOS and Linux. (Darwin = mac, xdg-open = linux).
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, output])

    try:
        # Pause for the length of the audio file, to allow for file to be read
        time.sleep(audio_length)
    except NameError:
        print('Could not detect audio length')

# Close the read pdf
pdfFileObj.close()

# Print the aggregated text from all pdf pages
print(text)
