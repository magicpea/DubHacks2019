from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

import io
import os

# Imports the Google Cloud client library


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'dubhacks12345-7231cf0cbad7.json'

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
#file_name = 'output.mp3'

file_name = 'noise.flac'

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config, audio)

print(len(response.results))

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))
    