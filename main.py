import os
import miditomp3

def listar(path):
    files = os.listdir(path)
    for f in files:
        print(f)


if __name__ == "__main__":

    path = "EDEN-midi/"
    listar(path)