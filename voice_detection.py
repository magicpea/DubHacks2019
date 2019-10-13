from google.cloud import speech_v1p1beta1
import io


def sample_recognize(local_file_path, langs):

    client = speech_v1p1beta1.SpeechClient()

    # local_file_path = 'resources/brooklyn_bridge.flac'

    # The language of the supplied audio. Even though additional languages are
    # provided by alternative_language_codes, a primary language is still required.
    language_code = langs[0]

    # Specify up to 3 additional languages as possible alternative languages
    # of the supplied audio.
    alternative_language_codes_element = langs[1]
    alternative_language_codes_element_2 = langs[2]
    alternative_language_codes = [
        alternative_language_codes_element,
        alternative_language_codes_element_2,
    ]
    config = {
        "language_code": language_code,
        "alternative_language_codes": alternative_language_codes,
    }
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config, audio)
    langs = []
    for result in response.results:
        # The language_code which was detected as the most likely being spoken in the audio
        langs.append(result.language_code)
        print(u"Translation: {}".format(result.language_code))
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))
    return langs