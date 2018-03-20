import os
import miditomp3
import numpy as np
import msgpack


def get_files(path):
    files = os.listdir(path)
    return files



if __name__ == "__main__":
    path = "EDEN-midi/"
    files = get_files(path)
    