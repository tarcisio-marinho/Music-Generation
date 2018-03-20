# Piano Music Generation with RNN with tensorflow

You can generate new piano music based with your prefered artists.

Pass as argument the path with the .mid files to the main.

If none argument is passed, it will use the EDEN playlist.

    python main.py -d <path>


You can also pass the name of the file, if not specified, it will be "output" 

    python main.py -o output_file

It will generate the output as .mp3 so you can listen to it!

If the quality of the output isn't that good, you can feed the program with more music.

# Dependencies

    sudo apt-get install timidity

    sudo apt-get install ffmpeg

    sudo pip install python-midi numpy msgpack tqdm tensorflow

    sudo pip install msgpack
    
# Usage

    usage: main.py [-h] [-d] [-o]

    Generate Piano music.

    optional arguments:
      -h, --help         show this help message and exit
      -d , --directory   the music to be trained should be inside this dir, if not
                         specified, EDEN-midi will be the input
      -o , --output      Output music as an .mp3 file, if not specified, will be
                         output.mp3
