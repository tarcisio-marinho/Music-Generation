import os
import miditomp3
import numpy as np
import msgpack
import midi_manipulation
import neuralnet

def get_files(path):
    songs = []
    for a, b, c in os.walk(path):
        for f in c:
            song = os.path.join(a, f)
            try:
                n = np.array(midi_manipulation.midiToNoteStateMatrix(song))
                songs.append(n)
            except Exception as e:
                print(e)
            
    return songs



if __name__ == "__main__":
    path = "EDEN-midi"
    songs = get_files(path)
    if(not os.path.isdir("generated")):
        os.mkdir("generated")

    neuralnet.menu(songs)