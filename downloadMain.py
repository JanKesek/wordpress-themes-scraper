import pickler
import downloader
import time

listOfUrls=pickler.Pickler.retrieve("badRegex", "../")
failedLinks=[]
for link in listOfUrls:
	try: downloader.Download.retrieve(link,link[32:].split('/')[0])
	except Exception as e:
		print(e)
		failedLinks.append(link)
		time.sleep(5)
