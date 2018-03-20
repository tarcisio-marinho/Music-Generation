import os
import miditomp3
import numpy as np
import msgpack
import midi_manipulation

def get_files(path):
    for a, b, c in os.walk(path):
        for f in c:
            print(os.path.join(a, c))



if __name__ == "__main__":
    path = "EDEN-midi/"
    get_files(path)
    #print(np.array(midi_manipulation.midiToNoteStateMatrix(files[1])))