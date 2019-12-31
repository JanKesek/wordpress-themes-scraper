from bs4 import BeautifulSoup
import requests
import re
import traceback
import pickle
import urllib3
soup = BeautifulSoup(open("mainHtml.html",'r'), "html.parser")
lst=soup.findAll('a', href=True)
print(len(lst))
