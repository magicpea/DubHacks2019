import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'DubHacks2019-d3f55594770d.json'

from record_audio import record_flac
from speech2text import speech2text
from txttranslate import translatetxt
from text2speech import text2speech
from audio2speaker import play_audio

filename = "output"

if __name__ == "__main__":
    record_flac(filename + ".wav")
    text = speech2text(filename + ".flac")[0]
    _, translated_text = translatetxt(text, 'es')
    text2speech(translated_text)
    play_audio(filename + ".mp3")

    