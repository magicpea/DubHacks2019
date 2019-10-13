from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

import io

# Imports the Google Cloud client library

# Instantiates a client
client = speech.SpeechClient()

def speech2text(input_file, lang):
    # Loads the audio into memory
    with io.open(input_file, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code=lang)

    # Detects speech in the audio file
    response = client.recognize(config, audio)
    transcript = []
    for result in response.results:
        transcript.append(result.alternatives[0].transcript)

    return transcript
    