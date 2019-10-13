from google.cloud import texttospeech
import os
filetxt = 'textTospeech/dubtxt.txt'
def textTranslatetoSpeech(file):
        
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/briansanchez/Downloads/Translate Project-49289bb13c3a.json'

        client = texttospeech.TextToSpeechClient()

        
        with open(file, 'r') as f:
                text= f.read()
                synthesis_input = texttospeech.types.SynthesisInput(text=text)

        voice = texttospeech.types.VoiceSelectionParams(
                language_code='en-EN',
                ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

        audio_config = texttospeech.types.AudioConfig(
                audio_encoding=texttospeech.enums.AudioEncoding.MP3)

        response = client.synthesize_speech(synthesis_input, voice, audio_config)

        with open('output.mp3', 'wb') as out:
                out.write(response.audio_content)
                print('Audio content written to file "output.mp3"')

textTranslatetoSpeech(filetxt)