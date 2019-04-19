import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
	return data[word]

word = input("Enter a word to get the meaning: ")
word = word.lower()
if(word in data):
	print(translate(word))


elif(len(get_close_matches(word, data.keys()))>0):
	print("is this your word? ",get_close_matches(word, data.keys())[0])
	inp = input("If yes then press 'y' otherwise press 'n': ")
	if(inp == 'y'):
		print(translate(get_close_matches(word, data.keys())[0]))
	elif(inp == 'n'):
		print("the word is wrong. please check..")
	else:
		print("Sorry Please Try Again..")


else:
	print("the word is wrong. please check..")

input()