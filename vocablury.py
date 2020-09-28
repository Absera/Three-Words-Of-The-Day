import json
import random

vocablury_file = open("vocablury.json", "r")
sent_words_file = open("sent_words.txt", "r+")
dictionary_file = open("dictionary.json", "r")

sent_words_read = sent_words_file.readlines()
vocablury_data = json.load(vocablury_file)
dictionary_data = json.load(dictionary_file)
sent_words = list(map(lambda x: x.strip(), sent_words_read))


def generateRandom():
	global vocablury_data, sent_words, sent_words_file, dictionary_data
	random_word = random.choice([i for i in vocablury_data])

	if random_word in sent_words:
		generateRandom()
	else:
		sent_words_file.write(random_word + "\n")

	try:
		random_word_definition = dictionary_data[random_word]
	except:
		random_word_definition = vocablury_data[random_word][1] # word definition

	generated = {
		"word": random_word,
		"type": vocablury_data[random_word][0], # word type
		"definition": random_word_definition
	}
	return generated


print()
