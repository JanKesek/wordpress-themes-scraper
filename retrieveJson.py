import pickle
import re
import requests
import time
import json
def retrieve(name):
	pickle_in=open(name+ ".pickle", "rb")
	return pickle.load(pickle_in)

lA=retrieve("listOfAuthors")
print("Regex not found: " + str(len(retrieve("badRegex"))))
print("Site not found: " + str(len(retrieve("subsitesNotFound"))))
print(len(retrieve("cssNotFound")))

newDict={}
for subsite in lA:
	t=[]
	for i in lA[subsite]:
		if len(i)!=0: 
			i=i[12:]
			t.append(i)

	if len(t)!=0 and len(i)>=5: newDict[subsite]=t

print(len(newDict))
with open('result.json', 'w') as fp:
	json.dump(newDict, fp)
#for site in newDict:
#	for i in newDict[site]:
#		print(i)
#		try:
#			resp=requests.get(i)
#			print(i+ str(resp.status_code))
#		except requests.exceptions.RequestException as e:  # This is the correct syntax
#			print("RequestException in CSS final")
#			time.sleep(5)
#			continue
#		except urllib3.exceptions.LocationParseError as e:
#			print(e.message)
#			time.sleep(5)
#			continue
