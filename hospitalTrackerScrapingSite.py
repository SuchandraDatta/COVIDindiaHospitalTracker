from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from configs import config as cfg

driver=webdriver.Chrome(executable_path=cfg.secret_info["executable_path_chrome_driver"])
driver.get("https://www.covid19india.org/")
try:
    element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '.state-name'))
    WebDriverWait(driver, 10).until(element_present)
    #As it's injected by JS, we have to wait for the entire stuff to load. Else #Selenium returns after only div id=root is loaded but not the rest of the #elements. The state class of the table contents is safe to use and guarantees #the page has indeed loaded
    #print("APP CLASS ELEMENT FOUND")
except:
    print("Timed out waiting for page to load")

dummyContent=driver.page_source
#print(dummyContent)
driver.quit()

from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(dummyContent, 'lxml')
step1=soup.find_all("div", class_="state-name")
all_rows=soup.find_all("div", class_="row")

#print("All divs state-name", step1)
states=[]
activeCases=[]

i=0
for rows in step1:
    stateName=re.findall(r'>[a-zA-Z\s]+<', str(rows))
    states.append(stateName)
    #print("State names: ", states)
    #print(all_rows[i])
    i=i+1
    #input("Stop")
    cell_statistics=BeautifulSoup(str(all_rows[i]), 'lxml')
    #cell_statistics.find_all("div", class_="is-confirmed")

    '''soup=BeautifulSoup(str(rows), 'lxml')
    step2=soup.find_all("td")

    cases=re.findall(r'[0-9][0-9,]+|[0-9]+', str(step2[2]))'''
    each_row=re.findall('<div class=\"total\" title=\"[0-9]+\">', str(cell_statistics))
    each_row=re.findall('title=\"[0-9]+\"', str(each_row[1]))
    each_row=each_row[0][7:-1]
    activeCases.append(each_row)

#print("Active cases: ", activeCases)
data_dict_array=[]
beds = {
    "Maharashtra":"120444",
    "Kerala":"77515",
    "Karnataka":"126498",
    "Uttar Pradesh":"129729",
    "Telangana":"38341",
    "Gujarat":"73409",
    "Rajasthan":"83692",
    "Delhi":"44955",
    "Tamil Nadu":"150148",
    "Madhya Pradesh":"66979",
    "Jammu and Kashmir":"22993",
    "Punjab":"31460",
    "Haryana":"25081",
    "Andhra Pradesh":"83937",
    "West Bengal":"409317",
    "Ladakh":"-1",
    "Assam":"-1",
    "Himachal Pradesh":"-1",
    "Jharkhand":"-1",
    "Bihar":"29815",
    "Andaman and Nicobar Islands":"2321",
    "Chandigarh":"4534",
    "Chhattisgarh":"23766",
    "Uttarakhand":"129729",
    "Goa":"5679",
    "Odisha":"35016",
    "Manipur":"3989",
    "Mizoram":"4309",
    "Puducherry":"8031",
    "Tripura":"-1",
    "Arunachal Pradesh":"-1",
    "Meghalaya": "-1",
    "Dadra and Nagar Haveli and Daman and Diu": "-1",
    "Nagaland": "-1",
    "Sikkim":"-1",
    "Lakshadweep":"-1"
                        }
for i in range(0, len(activeCases)-1):
    data_dict_term={}
    data_dict_term["state"]=states[i][0][1:-1]
    data_dict_term["activeCases"]=activeCases[i]
    if(beds[data_dict_term["state"]] == "-1"):
        data_dict_term["totalBeds"]="Not known"
        data_dict_term["bedsLeft"]="Not known"
    else:
        data_dict_term["totalBeds"]=beds[data_dict_term["state"]]
        data_dict_term["bedsLeft"]=int(data_dict_term["totalBeds"]) - int(data_dict_term["activeCases"])
    data_dict_array.append(data_dict_term)

#print(data_dict_array)
import json
#print("Length of datadict: " , len(data_dict_array))
json_string=json.dumps(data_dict_array)
print(json_string)#Printing the data is needed so that JavaScript can access the value directly using Newprocess.stdout.on
with open('./data/dataFromScraping.json', 'w+') as f:
    json.dump(data_dict_array, f)
