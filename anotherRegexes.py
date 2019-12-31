import pickle
import re
import requests
import time
import json
def retrieve(name):
	pickle_in=open(name+ ".pickle", "rb")
	return pickle.load(pickle_in)

listOfSites=retrieve("badRegex")
print(len(listOfSites))
print(listOfSites)
for i in listOfSites:
	try:
		resp=requests.get(i).text
		print("================ANOTHER ONE YOU FUCK=============================")
		author=re.findall(r"\nAuthor URI: .*\n", resp, re.M)
		if len(author)==0: author=re.findall(r"\nauthor uri: .*\n", resp, re.M)
		#if len(author)==0: author=re.findall(r"\nAuthor: .*\n", resp, re.M)
		print(str(author) + " " + i)
	except requests.exceptions.RequestException as e:
		print("JAPIERDOLE")
