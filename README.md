# pink-floyd-lyric-generator
A simple and terrible Pink Floyd lyrics generator based on Markov chains (and written in Python).

The used lyrics (available under *lyrics/* folder) were parsed from [Vagalume.com.br](http://www.vagalume.com.br) through the [vagalume-download-lyrics](https://github.com/paladini/vagalume-download-lyrics) project. Note that the lyrics are not very clean, containing some dirty words/characters (I'll try to fix that soon). The lyrics are used for studying purposes only (about how to generate lyrics based on the Markov chains approach), no copyright infringement intended.

The current results are quite bad, but I'll try to improve this repository until the project can generate (and really generate) good lyrics (and of course, similar to Pink Floyd lyrics). 

### Dependencies
- [PyMarkovChain](https://github.com/TehMillhouse/PyMarkovChain) (install it using `pip3 install PyMarkovChain`)
- [vagalume-download-lyrics](https://github.com/paladini/vagalume-download-lyrics) (don't need to install, I just have used it to parse Pink Floyd lyrics from Vagalume).
- Python 3

### Usage
The program expects the following arguments:
```bash
python3 pink-floyd-lyric-generator.py <number_of_phrases_to_generate>
```

For example, if you want to generate 10 sentences:
```bash
python3 pink-floyd-lyric-generator.py 10
```

When I ran the script, I got the following output:
```sh
So ya
We don't need no education
But now he's resigned to his fate
All of this temptation, it turned my faith to lies
Corporal Clegg had a big pin, a little place of their lives
And starts to climb
Does anybody else in here tonight
Don't be afraid to care
Rise And Shine
Just the basic facts
```

If you want to reset the database, just run the following:
```sh
chmod +x clean_db.sh
./clean_db.sh
```

### How it works?
This's my second experiment with lyrics generation using Markov chains, but I've read some texts and a lot of examples before creating it. In order to understand how can I generate lyrics, please check the following links:

- [Lyricize: A Flask App to Create Lyrics Using Markov Chains](https://realpython.com/blog/python/lyricize-a-flask-app-to-create-lyrics-using-markov-chains/) [very useful]
- [Text generation with Markov chains](https://lauris.github.io/text-generation-markov-chain)
- [Generating pseudo random text with Markov chains using Python](http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/)

And here you can check some projects on Github that helped me:
- [Lyrics Can Be Easy](https://github.com/zeyus/lyrics-can-be-easy)
- [taytay](https://github.com/caktus/taytay) [Taylor-Swift-like lyric generator, I really want to read their code, they have awesome results]
- [PyMarkovChain](https://github.com/TehMillhouse/PyMarkovChain)
- [py-simple-lyric-generator](https://github.com/paladini/pink-floyd-lyric-generator/) [My first experiment related to lyric generation and Markov chains.]

### About
The `pink-floyd-lyric-generator` was created by Fernando Paladini on 01-22-2016, but it was heavily based on another open-source projects you can find at the web. If you have any issue, doubt, problem or suggestion, please feel free to create a [new Issue](https://github.com/paladini/pink-floyd-lyric-generator/issues) or even contact me at fnpaladini at gmail dot com. 

