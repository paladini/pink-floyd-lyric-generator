#!/usr/bin/python3
import sys
import os
import glob
from pymarkovchain import MarkovChain

if __name__ == '__main__':

    # Checking and saving arguments
    if len(sys.argv) != 2:
        raise "Usage: python3 pink-floyd-lyric-generator.py [number_of_phrases_to_generate]"
    number_of_phrases = sys.argv[1]

    # Generating a Markov Chain Model
    db_name = "db/pink_floyd.db"
    mc = MarkovChain(db_name)

    # Checking if the database already exists, if so uses the cache instead another API call
    if not os.path.isfile(db_name):
        print("No data cached. Please be patient while we parse the lyrics from the folder 'lyrics'.")      
        
        # Adding lyrics to a single gigant string
        lyrics = ''

        for filename in glob.glob(os.path.join('lyrics/', '*.lyric')):
            with open(filename, 'r') as lyric:
                lyrics += lyric.read()

        
        # Generating the database
        mc.generateDatabase(lyrics)
        mc.dumpdb()

    # Printing a string
    for i in range(0, int(number_of_phrases)):
        print(mc.generateString())