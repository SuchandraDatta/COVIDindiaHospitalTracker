import requests
userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
headers={'User-Agent' : userAgent}


#regOBJ=requests.get('https://www.mohfw.gov.in/pdf/DistrictWiseList324.pdf', headers=headers)

#open('./dummy.pdf', 'wb').write(regOBJ.content)

#print(regOBJ.content)

# importing required modules 
import PyPDF2 
  
# creating a pdf file object 
pdfFileObj = open('dummy.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# printing number of pages in pdf file 
print(pdfReader.numPages) 
totalPages=pdfReader.numPages 
pageNumber=0
pageText=""

# creating a page object 
for i in range(0, pdfReader.numPages):
    pageObj = pdfReader.getPage(i) 
    # extracting text from page 
    pageText=pageText+pageObj.extractText()

print(pageText)
#Convert to JSON
step1=pageText.split("\n")
#print(step1)
step2=[]
for x in step1:
    if(x!=' ' and x!='*'):
        step2.append(x)
print(step2)

dataDict={}
pos=7

while(pos<=len(step2) and step2[pos]!='Total'):
    stateCount=0
    distNumber=0
    state=""
    state=step2[pos]
    pos=pos+1
    if(state=='Goa'):
        stateCount=step2[pos+1]
        distNumber=-96
    elif(state=='Karnataka'):
        distNumber=10
    else:
        distNumber=int(step2[pos])
    if(step2[pos+1]=='#'):
        i=0
    else:
        i=1
    if(state=='Karnataka'):
        i=0
    pos=pos+2
    

    if(distNumber==1):
        if((step2[pos][0]>='A' and step2[pos][0]<='Z')):
            pos=pos+1
        elif((step2[pos][0]>='a' and step2[pos][0]<='z')):
            print("HAHAHAH")
            pos=pos+1
        stateCount=step2[pos]
        pos=pos+1
    else:
        while(i<=distNumber):
            if(step2[pos][0]>='A' and step2[pos][0]<='Z'):
                print("Here")
            elif((step2[pos][0]>='a' and step2[pos][0]<='z')):
                print("HAHAHAH")
            else:
                stateCount=stateCount+int(step2[pos])
                print("\nAdding: ", step2[pos])
                i=i+1
            pos=pos+1
        #pos=pos+1#Last line of each state-wise block    
    print("For: ", state, "Count: " , stateCount)
    dataDict[state]=stateCount

import json
json_string = json.dumps(dataDict)
print(json_string)
with open('dummyAgain.json', 'w+') as fileToWrite:
    json.dump(dataDict, fileToWrite)

# closing the pdf file object 
pdfFileObj.close() 


