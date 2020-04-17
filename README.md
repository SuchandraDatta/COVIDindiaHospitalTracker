# COVIDindiaHospitalTracker

Tried to make a website that displays state-wise the number of active COVID-19 cases in India and the approximate number of hospital beds that remains for servicing patients(these patients may or maynot be affected by COVID-19). It is noted that the number of hospital beds per state has been obtained from https://www.kaggle.com/sudalairajkumar/covid19-in-india which in turn have got the data from https://pib.gov.in/PressReleasePage.aspx?PRID=1539877. Values are subject to change and should be treated as an approximation. 

Tech used to realize this

:herb: Python has been employed to obtain the number of active cases, state-wise from covid19india.org. At first requests module was used but later it was found that the table in the page is injected by JavaScript after it loads so the html cannot be obtained using requests or urllib. Selenium was used to get the html of the page.

:herb: Once the html is extracted, the table was parsed using the powerful BeautifulSoup library in Python. The names of states and the corresponding active cases were extracted and stored in a json file.

:herb:A node.js server was set up to serve pages that uses AngularJS. Server is set up without using express. Within the server, whenever the requested page is the one that displays the table(state and hospital beds), the python script is executed by spawning a child process. Once done, the data is obtained via a get request from within the controller of the angular app and rendered to the screen via simple angular directives like ng-repeat.


![pic](https://user-images.githubusercontent.com/41965125/77928463-0dde8780-72c6-11ea-9cc5-c2732f3c651c.png)

