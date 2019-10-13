from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

import io
import os

# Imports the Google Cloud client library


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'DubHacks2019-d3f55594770d.json'

# Instantiates a client
client = speech.SpeechClient()

def speech2text(input_file):
    # Loads the audio into memory
    with io.open(input_file, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='en-US')

    # Detects speech in the audio file
    response = client.recognize(config, audio)
    transcript = []
    for result in response.results:
        transcript.append(result.alternatives[0].transcript)

    return transcript
    