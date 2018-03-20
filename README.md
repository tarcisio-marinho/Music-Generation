# Piano Music Generation with RNN with tensorflow

You can generate new piano music based with your prefered artists.

Pass as argument the path with the .mid files to the main.

If none argument is passed, it will use the EDEN playlist.

    python main.py <path>

It will generate the output as .mp3 so you can listen to it!

If the quality of the output isn't that good, you can feed the program with more music.

# Dependencies

    sudo apt-get install timidity

    sudo apt-get install ffmpeg

    sudo pip install python-midi numpy msgpack tqdm tensorflow

    sudo pip install msgpack
