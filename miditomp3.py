import os, subprocess

def midi_to_mp3(path):

    output = os.path.splitext(path)[0] + ".mp3"

    command = "timidity {} -Ow -o - | ffmpeg -i - -acodec libmp3lame -ab 64k {}".format(path, output)
    os.system(command)
