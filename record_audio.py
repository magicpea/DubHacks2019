import sounddevice as sd
#import noisereduce as nr
from scipy.io.wavfile import write
from os.path import splitext
from pydub import AudioSegment


def record(filename):
    fs = 16000  # Sample rate
    seconds = 10  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    print('Recording...')
    sd.wait()  # Wait until recording is finished
    print('Done!')
    write(filename, fs, myrecording)  # Save as WAV file


'''
#
# load data
rate, data = wavfile.read("noise.wav")
# select section of data that is noise
noisy_part = data[10000:15000]
# perform noise reduction
reduced_noise = nr.reduce_noise(audio_clip=data, noise_clip=noisy_part, verbose=True)
'''

def wav2flac(wav_path):
    flac_path = "%s.flac" % splitext(wav_path)[0]
    song = AudioSegment.from_wav(wav_path)
    song.export(flac_path, format = "flac")

def record_flac(filename):
    record(filename)
    wav2flac(filename)

