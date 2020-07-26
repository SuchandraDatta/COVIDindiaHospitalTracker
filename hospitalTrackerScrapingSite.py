from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

'''check='<html><body><div class="row"><div class="cell"><div class="state-name fadeInUp">Tamil Nadu</div><span class="Tooltip" style="position: relative;"><svg fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="16" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10"></circle><line x1="12" x2="12" y1="16" y2="12"></line><line x1="12" x2="12.01" y1="8" y2="8"></line></svg><div></div></span></div><div class="cell statistic"><div class="delta is-confirmed"></div><div class="total">2,06,737</div></div><div class="cell statistic"><div class="total">52,273</div></div><div class="cell statistic"><div class="delta is-recovered"></div><div class="total">1,51,055</div></div><div class="cell statistic"><div class="delta is-deceased"></div><div class="total">3,409</div></div><div class="cell statistic"><div class="delta is-tested"></div><div class="total">2.3M</div></div></div></body></html>'
#<div class="cell statistic"><div class="total">52,273</div></div>
import re
got_this=re.findall('<div class=\"total\">[0-9][0-9,]+</div>', str(check))
got_this=got_this[1][19:-6]
print(got_this)'''

driver=webdriver.Chrome(executable_path="C:\\Users\\Suchandra Datta\\chromedriver_win32\\chromedriver")
driver.get("https://www.covid19india.org/")
try:
    element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '.state-name'))
    WebDriverWait(driver, 10).until(element_present)
    #As it's injected by JS, we have to wait for the entire stuff to load. Else #Selenium returns after only div id=root is loaded but not the rest of the #elements. The state class of the table contents is safe to use and guarantees #the page has indeed loaded
    print("APP CLASS ELEMENT FOUND")
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

print("All divs state-name", step1)
states=[]
activeCases=[]

i=0
for rows in step1:
    stateName=re.findall(r'>[a-zA-Z\s]+<', str(rows))
    states.append(stateName)
    print("State names: ", states)
    #print(all_rows[i])
    i=i+1
    #input("Stop")
    cell_statistics=BeautifulSoup(str(all_rows[i]), 'lxml')
    cell_statistics.find_all("div", class_="is-confirmed")
    #print(cell_statistics)
    #input("Stop")
    '''soup=BeautifulSoup(str(rows), 'lxml')
    step2=soup.find_all("td")

    cases=re.findall(r'[0-9][0-9,]+|[0-9]+', str(step2[2]))'''
    each_row=re.findall('<div class=\"total\">[0-9][0-9,]+</div>', str(cell_statistics))
    each_row=each_row[1][19:-6]
    #print(each_row)
    #input("Stop")
    activeCases.append(each_row)

print("Active cases: ", activeCases)
data_dict_array=[]
for i in range(0, len(activeCases)-1):
    data_dict_term={}
    data_dict_term["state"]=states[i][0][1:-1]
    data_dict_term["activeCases"]=activeCases[i]
    data_dict_array.append(data_dict_term)

print(data_dict_array)
import json
print("Length of datadict: " , len(data_dict_array))
json_string=json.dumps(data_dict_array)
print(json_string)
with open('dataFromScraping.json', 'w+') as f:
    json.dump(data_dict_array, f)
