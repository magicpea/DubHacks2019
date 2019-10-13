from google.cloud import texttospeech

def text2speech(text):
        client = texttospeech.TextToSpeechClient()

        input_text = texttospeech.types.SynthesisInput(text=text)

        voice = texttospeech.types.VoiceSelectionParams(
            language_code = 'es-MX',
            ssml_gender = texttospeech.enums.SsmlVoiceGender.FEMALE)

        audio_config = texttospeech.types.AudioConfig(
            audio_encoding  = texttospeech.enums.AudioEncoding.MP3)

        response = client.synthesize_speech(input_text, voice, audio_config)

        with open('output.mp3', 'wb') as out:
                out.write(response.audio_content)
                print('Audio content written to file "output.mp3"')
        
#textTranslatetoSpeech("we bout to rob a wells fargo, we bout to steal a whole car load.")