from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver=webdriver.Chrome(executable_path="C:\\Users\\Suchandra Datta\\chromedriver_win32\\chromedriver")
driver.get("https://www.covid19india.org/")
try:
    element_present = EC.presence_of_element_located((By.CSS_SELECTOR, 'Navbar'))
    WebDriverWait(driver, 10).until(element_present)
except:
    print("Timed out waiting for page to load")

dummyContent=driver.page_source
#print(dummyContent)
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



