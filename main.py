import os
import miditomp3
import numpy as np
import msgpack
import midi_manipulation
import neuralnet
import sys
import merge
import argparse

parser = argparse.ArgumentParser(description='Generate Piano music.')
parser.add_argument('-d', '--directory', type = str, required = False, metavar = '',  help = 'the music to be trained should be inside this dir, if not specified, EDEN-midi will be the input')
parser.add_argument('-o', '--output', type = str, required = False, metavar = '',  help = 'Output music as an .mp3 file, if not specified, will be output.mp3')
args = parser.parse_args()


def get_files(path):
    songs = []
    for a, b, c in os.walk(path):
        for f in c:
            song = os.path.join(a, f)
            try:
                n = np.array(midi_manipulation.midiToNoteStateMatrix(song))
                songs.append(n)
            except Exception as e:
                print("error: {} on file: {}".format(e, f))
            
    return songs



if __name__ == "__main__":
    
    #default directory for musics
    path = "EDEN-midi"
    output = "output"

    if(args.directory):
        path = args.directory
    
    if(args.output):
        output = args.output
        
    songs = get_files(path)
    if(not os.path.isdir("generated")):
        os.mkdir("generated")

    neuralnet.menu(songs)
    merge.menu(output)