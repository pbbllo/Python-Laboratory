import boto3
import os
import sys
import subprocess

from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
from tempfile import gettempdir

def sync(text):
    AmazonPolly = boto3.client('polly')

    try:
        response = AmazonPolly.synthesize_speech(Text=text, OutputFormat='mp3', VoiceId='Joanna')
    except (BotoCoreError, ClientError) as error:
        print(error)
        sys.exit(-1)
    
    return response


def execute(text):
    AmazonPolly = sync(text)

    # Access the audio stream from the response
    if "AudioStream" in AmazonPolly:
            with closing(AmazonPolly["AudioStream"]) as stream:
                output = os.path.join(gettempdir(), "speech.mp3")
                try:
                # Open a file for writing the output as a binary stream
                    with open(output, "wb") as file:
                        file.write(stream.read())
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