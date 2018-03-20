import os
import miditomp3
import numpy as np
import msgpack
import midi_manipulation

def get_files(path):
    songs = []
    for a, b, c in os.walk(path):
        for f in c:
            songs.append(os.path.join(a, f))

    return songs



if __name__ == "__main__":
    path = "EDEN-midi/"
    songs = get_files(path)