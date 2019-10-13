import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Path to Google Credentials .json file'

from record_audio import record_flac
from speech2text import speech2text
from txttranslate import translatetxt
from text2speech import text2speech
from audio2speaker import play_audio
from voice_detection import sample_recognize

filename = "output"
outputlang = "en"
langs = ['es', 'en', 'fr']

if __name__ == "__main__":
    record_flac(filename + ".wav")
    detected_lang = sample_recognize(filename + ".flac", langs)[0]
    print(detected_lang)
    text = speech2text(filename + ".flac", detected_lang)[0]
    _, translated_text = translatetxt(text, outputlang)
    text2speech(translated_text, outputlang)
    play_audio(filename + ".mp3")

    
