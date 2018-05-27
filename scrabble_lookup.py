from flask import Flask, render_template

app = Flask(__name__)

# Populate our dictionary with a sample Scrabble dictionary taken from
# https://raw.githubusercontent.com/jonbcard/scrabble-bot/master/src/dictionary.txt
dictionary_words = []

with open('./scrabble_dictionary.txt') as file:
    for line in file:
    	word = line.strip().lower() # Make all words lower case so we don't worry about case sensitivity in our searching
    	dictionary_words.append(word)


@app.route('/')
def get_landing_page():
    return render_template('index.html')

@app.route('/lookup/<word>')
def lookup_word(word):
    if word.strip().lower() in dictionary_words:
      return render_template('response.html', word=word, points = count_scrabble_points(word), match=True)
    else:
      return render_template('response.html', word=word, match=False)

# Using point values from https://scrabble.hasbro.com/en-us/faq
def count_scrabble_points(word):
	letters_to_points = {
		"a" : 1, 
		"e" : 1,
		"i" : 1,
		"o" : 1,
		"u" : 1,
		"l" : 1,
		"n" : 1,
		"s" : 1,
		"t" : 1,
		"r" : 1,
		"d" : 2,
		"g" : 2,
		"b" : 3,
		"c" : 3,
		"m" : 3,
		"p" : 3,
		"f" : 4,
		"h" : 4,
		"v" : 4,
		"w" : 4,
		"y" : 4,
		"k" : 5,
		"j" : 8,
		"x" : 8,
		"q" : 10,
		"z" : 10
		}
	points = 0

	for letter in word:
		points = points + letters_to_points.get(letter)

	return points
