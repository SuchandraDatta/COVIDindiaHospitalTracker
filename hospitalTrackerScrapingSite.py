from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\Users\\Suchandra Datta\\chromedriver_win32\\chromedriver")
driver.get("https://www.covid19india.org/")

dummyContent=driver.page_source
driver.quit()

from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(dummyContent, 'lxml')
step1=soup.find_all("tr", class_="state")
states=[]
activeCases=[]


for rows in step1:
    stateName=re.findall(r'>[a-zA-Z\s]+<', str(rows))
    states.append(stateName)

    soup=BeautifulSoup(str(rows), 'lxml')
    step2=soup.find_all("td")

    cases=re.findall(r'[0-9][0-9,]+|[0-9]+', str(step2[2]))

    activeCases.append(cases)

data_dict_array=[]
for i in range(0, len(activeCases)-1):
    data_dict_term={}
    data_dict_term["state"]=states[i][0][1:-1]
    data_dict_term["activeCases"]=activeCases[i][0]
    data_dict_array.append(data_dict_term)

print(data_dict_array)
import json
print("Length of datadict: " , len(data_dict_array))
json_string=json.dumps(data_dict_array)
print(json_string)
with open('dataFromScraping.json', 'w+') as f:
    json.dump(data_dict_array, f)