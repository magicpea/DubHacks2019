
from pydub import AudioSegment
from pydub.playback import play

# Takes a .mp3 file as a parameter, converts it to a
# .wav file, and plays the audio from that file
def play_audio(fileName):

    # Takes an audio segment from the given mp3 file
    song = AudioSegment.from_mp3(fileName)

    # Assigns a new file name, basically adds the end
    # tag ".wav" instead of ".mp3"
    newName = (fileName[:-4]) + ".wav"

    # Exports the song to a wav with the new name
    song.export(newName, format = "wav")

    # Outputs the audio file, plays out loud onto 
    # either computer or device connected 
    play(song)








