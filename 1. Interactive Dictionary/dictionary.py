import json
from difflib import get_close_matches

def search(term):
	data = json.load(open("data.json"))
	
	if term in data:
		return data[term]

	elif term.title() in data:
		return data[term.title()]

	elif term.upper() in data:
		return data[term.upper()]

	elif len(get_close_matches(term, data.keys(), cutoff = 0.8)) > 0:
		reply = input("Did you mean "+ get_close_matches(term, data.keys())[0]+":(y/n) ")

		if reply.lower() == "y":
			return data[get_close_matches(term, data.keys())[0]]

		elif reply.lower() == "n":
			return "Not found"

		else:
			return "Invalid input"

	else:
		return "Not found."

def userInput():
	term = input("Enter the word: ")
	return (search(term))

meaning = userInput()
if type(meaning) == list:
	for i in meaning:
		print(i)
else:
	print (meaning)

