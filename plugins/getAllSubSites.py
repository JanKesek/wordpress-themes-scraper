from bs4 import BeautifulSoup
import requests
import re
import traceback
import pickle
import urllib3
import socket
import time
def save(name, obj):
    pickle_out=open(name + ".pickle", "wb")
    pickle.dump(obj, pickle_out)
    pickle_out.close()
def retrieve(name):
    pickle_in=open(name+ ".pickle", "rb")
    return pickle.load(pickle_in)

soup = BeautifulSoup(open("index.html",'r'), "html.parser")
listOfSubsites=[]
for tag in soup.findAll('a', href=True):
    listOfSubsites.append(tag['href'])
dictionaryOfUrls={}
unfinishedRegexex=[]
subsitesNotFound=[]
cssNotFound=[]
print(len(listOfSubsites))
for subsite in listOfSubsites:
    print("THIS IS SUBSITE: "+ subsite)
    try:
        htmlcontent=requests.get("https://plugins.svn.wordpress.org/"+subsite, timeout=10)
        versionsSubsites=BeautifulSoup(htmlcontent.text, "html.parser")
        listOfAllSubsites = versionsSubsites.findAll('a', href=True)
        for tag in listOfAllSubsites:
            if tag['href']=="trunk/":
                print(tag['href'])
                url="http://plugins.svn.wordpress.org/"+subsite+tag['href']+"readme.txt"
                try:
                    print(url)
                    cssFile=requests.get(url, timeout=10)
                    author=re.findall(r"\nDonate .*: .*\n", cssFile.text, re.M)
                    print(author)
                    if len(author)==0: 
                        author=re.findall(r"\nLicence URI: .*\n",cssFile.text, re.M)
                    if len(author)==0: author=re.findall(r"\nLicence Link: .*\n", cssFile.text, re.M)
                    if len(author)==0: unfinishedRegexex.append(url) 
                    dictionaryOfUrls[subsite]=author
                    break
                except TimeoutError as te:
                    print("TimeoutError in CSS Will retry")
                    time.sleep(5)
                    cssNotFound.append(url)
                    continue
                except urllib3.exceptions.NewConnectionError as e:
                    print("NewConnectionError in CSS Will retry")
                    cssNotFound.append(url)
                    time.sleep(5)
                    continue
                except urllib3.exceptions.MaxRetryError as e:
                    print("MaxRetryError in CSS Will Retry")
                    time.sleep(5)
                    cssNotFound.append(url)
                    continue
                except requests.exceptions.ConnectionError as ce:
                    print("ConnectionError in CSS: Will Retry")
                    time.sleep(5)
                    cssNotFound.append(url)
                    continue
                except socket.timeout as te:
                    print("socket.timeout in CSS Will retry")
                    time.sleep(5)
                    cssNotFound.append(url)
                    continue
                except requests.exceptions.RequestException as e:  # This is the correct syntax
                    print("RequestException in CSS final")
                    time.sleep(5)
                    cssNotFound.append(url)
                    continue
    except TimeoutError as te:
        print("TimeoutError in Subsite Will retry")
        time.sleep(5)
        subsitesNotFound.append(subsite)
        continue
    except socket.timeout as te:
        print("socket.timeout in Subsite Will retry")
        time.sleep(5)
        subsitesNotFound.append(subsite)
        continue
    except requests.exceptions.Timeout as te:
        print("requests.exceptions.Timeout in Subsite Will retry")
        time.sleep(5)
        subsitesNotFound.append(subsite)
        continue
    except requests.exceptions.ConnectionError as ce:
        print("ConnectionError in Subsite: Will Retry")
        time.sleep(5)
        subsitesNotFound.append(subsite)
        continue
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print("RequestException in Subsite: final") 
        time.sleep(5)
        subsitesNotFound.append(subsite)
        continue
print(dictionaryOfUrls)
print(unfinishedRegexex)
save("listOfAuthors", dictionaryOfUrls)
save("badRegex", unfinishedRegexex)
save("subsitesNotFound", subsitesNotFound)
save("cssNotFound", cssNotFound)
save("listOfAllSubsites", listOfSubsites)
