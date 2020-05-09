'''dummyContent=[
    '<tr class="state"><td><div class="title-chevron"><span class="dropdown rotateDownRight"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg></span><span class="title-icon">Maharashtra<span data-tip="[05-May]<br>- Total numbers are updated to the final figure reported for 05th May. <br>- 796 cases added by MH govt. on 4th May due to data cleaning <br>- 143 cases added by MH govt. on 5th May due to data cleaning <br>" data-event="touchstart mouseover" data-event-off="mouseleave" currentitem="false"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg></span></span></div></td><td><span class="delta is-confirmed"></span><span class="total">19,063</span></td><td><span class="delta is-active"></span><span class="total">14,862</span></td><td><span class="delta is-recovered"></span><span class="total">3,470</span></td><td><span class="delta is-deaths"></span><span class="total">731</span></td></tr><tr class="state"><td><div class="title-chevron"><span class="dropdown rotateDownRight"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg></span><span class="title-icon">Gujarat<span data-tip="" data-event="touchstart mouseover" data-event-off="mouseleave" currentitem="false"></span></span></div></td><td><span class="delta is-confirmed"></span><span class="total">7,403</span></td><td><span class="delta is-active"></span><span class="total">5,082</span></td><td><span class="delta is-recovered"></span><span class="total">1,872</span></td><td><span class="delta is-deaths"></span><span class="total">449</span></td></tr>'
]'''
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
    #print("Working on", rows)
    #duh=input("hello world")

    stateName=re.findall(r'>[a-zA-Z\s]+<', str(rows))
    states.append(stateName)
    #print("State: ", stateName)
    #duh=input("Oh no dude")
    soup=BeautifulSoup(str(rows), 'lxml')
    step2=soup.find_all("td")
    #print("Active cases: ", step2[2])
    cases=re.findall(r'[0-9][0-9,]+|[0-9]+', str(step2[2]))
    
    #print("Cases: ", cases[0])
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