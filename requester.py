from bs4 import BeautifulSoup
import requests
import re
import traceback
import pickler
import urllib3
import socket
import time

class Requester:
	def __init__(self, listOfSubsites, regexString, filename):
		self.listOfSubsites=listOfSubsites
		self.regexString=regexString
		self.filename=filename
	def search(self):
		for subsite in self.listOfSubsites:
			print("THIS IS SUBSITE: "+ subsite)
			try:
				htmlcontent=requests.get("https://plugins.svn.wordpress.org/"+subsite, timeout=10)
				versionsSubsites=BeautifulSoup(htmlcontent.text, "html.parser")
				for tag in versionsSubsites.findAll('a', href=True):
					if tag['href']=='trunk/':
						print(tag['href'])
						url="http://plugins.svn.wordpress.org/"+subsite+tag['href']+"readme.txt"
						try:
							print(url)
							cssFile=requests.get(url, timeout=10)
							author=re.findall(self.regexString, cssFile.text, re.M)
							print(author)
							if len(author)==0: unfinishedRegexex.append(url) 
							else dictionaryOfUrls[subsite]=author
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
		p=Pickler(...)
		p.save(dictionaryOfUrls,"listOfAuthors2")
		p.save(unfinishedRegexex,"badRegex")
		p.save(subsitesNotFound,"subsitesNotFound")
		p.save(cssNotFound,"cssNotFound")

