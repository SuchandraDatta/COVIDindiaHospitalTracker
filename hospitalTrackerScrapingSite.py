from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\Users\\Suchandra Datta\\chromedriver_win32\\chromedriver")
driver.get("https://www.covid19india.org/")

dummyContent=driver.page_source
print(dummyContent)
driver.quit()

print(dummyContent)
from bs4 import BeautifulSoup
soup = BeautifulSoup(dummyContent, 'lxml')


getStates=soup.find_all("tr", class_="state")
for i in range(0, len(getStates)):
    print(getStates[i])

import re
states=[]
states=re.findall(r'>[a-zA-Z\s]+<', str(getStates))    
print(states)
print("No. of states: ", len(states))


allCases=[]
#allCases=re.findall(r'<td style="color: rgb\(181, 181, 181\);">-</td>|<td style="color: inherit;">[0-9]+</td>', str(getStates))
allCases=re.findall(r'<td style="color: inherit;">[0-9]+[,]*[0-9]+</td>|<td style="color: inherit;">[0-9]*</td>', str(getStates))


eachStateCase=[]
dataDict=[]
i=0
pos=0
while(i<len(allCases)-1):
    confirmedCases=re.findall(r'>[0-9]+[,]*[0-9]+<|>[0-9]*<', str(allCases[i]))
    key=states[pos][1:-1]
    pos=pos+1
    print(confirmedCases)
    if(len(confirmedCases)>0):
        dataDictTerm={}
        dataDictTerm["state"]=key
        dataDictTerm["activeCases"]=confirmedCases[0][1:-1]
        dataDict.append(dataDictTerm)
        #dataDict[key]=confirmedCases[0][1:-1]
        print("key ", key, " value", confirmedCases[0][1:-1])
    i=i+1

import json
print("Length of datadict: " , len(dataDict))
json_string=json.dumps(dataDict)
print(json_string)
with open('dataFromScraping.json', 'w+') as f:
    json.dump(dataDict, f)