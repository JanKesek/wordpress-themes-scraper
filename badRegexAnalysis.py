import requests
import pickle
import re

def retrieve(name):
	pickle_in=open(name+ ".pickle", "rb")
	return pickle.load(pickle_in)
def save(name, obj):
	pickle_out=open(name + ".pickle", "wb")
	pickle.dump(obj, pickle_out)
	pickle_out.close()

def readFirstLines(lst):
	generalIter=0
	iterOfGoodsites=0

	badSites=[]
	goodSites={}
	for i in lst:
		try:
			t=requests.get(i).text
			#print("\n\n\n\n\n\nFIRST 500 CHARS FOR\n" + i + "\n")
			#string="".join(list(t)[0:700])
			#author=re.findall(r"(\n(((a|A)uthor)|(AUTHOR)) ((uri)|(URI)|(Uri))*: ((htt.*)|(www.*))\n)", t, re.M)
			#author=re.findall(r"\n .* (htt.*)|(www.*) .*\n", t,re.M)
			reg=r"^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:/[^\s]*)?$"
			#author=re.findall(r"(htt.*)|(www.*)",re.compile(r"(\n .* (htt.*)|(www.*) .* \n)",t))
			author=re.findall(reg,t,re.M)
			z=[]
			if len(author)!=0:
				print(author)
				print(generalIter)
				goodSites[i]=author
			generalIter+=1	
			#if len(author)!=0:
			#	for j in author[0]:
			#		res=re.findall(r"(htt.*)|(ww.*)", j)
			#		if len(res)!=0: 
			#			z.append(res)
			#			iterOfGoodsites+=1
			#		else: badSites.append(i)
			#if len(z)!=0: 
			#	print(z[0][0])
			#	print(generalIter)
			#generalIter=generalIter+1
		except requests.exceptions.RequestException as e:
			print("Bad connection or smth")
		  # This is the correct syntax
	#print(iterOfGoodsites)
	#print(len(badSites))
	#save("furtherBadSites2", badSites)
	save("someURLSofSites", goodSites)
lst=retrieve("badRegex")
readFirstLines(lst)
