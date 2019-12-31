import pandas as pd
class Lowercaser:
    def __init__(self):
        self.text={}
    def add(self,text):
        url=list(text.keys())[0]
        self.text[url]=pd.DataFrame(text)
    def convert(self, url):
        fileTxt=[]
        for i, r in self.text[url].iterrows():
            #print(r[url])
            lst=r[url].split(" ")
            for j in range(len(lst)): 
                lst[j]=lst[j].lower()
            r[url]=" ".join(lst)
            fileTxt.append(r[url])
            #print(r[url])
        ret= " ".join(fileTxt)
        print(ret)
        return ret

