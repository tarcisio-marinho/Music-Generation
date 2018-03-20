import os, subprocess

def midi_to_mp3(path):

    saida = os.path.splitext(path)[0] + ".mp3"

    comando = "timidity {} -Ow -o - | ffmpeg -i - -acodec libmp3lame -ab 64k {}".format(path, saida)
    os.system(comando)
