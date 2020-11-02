# COVIDindiaHospitalTracker

Tried to make a website that displays state-wise the number of active COVID-19 cases in India and the approximate number of hospital beds that remains for servicing patients(these patients may or may not be affected by COVID-19, it displays the number of beds that may be used for servicing patients inflicted with covid-19 or other ailments). It is noted that the number of hospital beds per state has been obtained from https://www.kaggle.com/sudalairajkumar/covid19-in-india which in turn have got the data from https://pib.gov.in/PressReleasePage.aspx?PRID=1539877. Values are subject to change and should be treated as an approximation. 

Tech used to realize this

:herb: Python has been employed to obtain the number of active cases, state-wise from covid19india.org. At first requests module was used but later it was found that the table in the page is injected by JavaScript(specifically as on 02-11-2020 React was being used) after it loads so the html cannot be obtained using requests or urllib. Selenium was used to get the html of the page.

:herb: Once the html is extracted, the table was parsed using the powerful BeautifulSoup library in Python. The names of states and the corresponding active cases were extracted and stored in a json file. As of 31-10-2020 the active cases has a class=total and the title of the element holds the number of active cases. All columns have a class=total, column 2 or index 1 element returned by findall is the one to be considered.

:herb:A node.js server was set up to serve pages that uses AngularJS. Server is set up without using express. Within the server, whenever the requested page is the one that displays the table(state and hospital beds), the python script is executed by spawning a child process. Once done, the data is obtained via a get request from within the controller of the angular app and rendered to the screen via simple angular directives like ng-repeat. Usage of Angular is not necessary, it is used simple as at that point of time I was learning the basics of Angular. Using Django we could have achieved the same functionality, that is, executing the Python script and displaying the output using views.py and Django template tags. 

Difficulties faced and updated:
1. Selenium returns the page as soon as it gets loaded but does not wait for the correspoding JavaScript to be injected to the page. So it is made to wait using expected conditions where the condition is that a css class element state-name has been loaded.
2. The driver for Selenium required frequent updation to match Chrome version.
3. Whenever the layout of the page is updated, it causes problems as extraction is heavily dependant on the class names of specific components.
4. To serve webp images, it is to be included in the list of accepted MIME times as image/webp.


![output_screenshot](https://user-images.githubusercontent.com/41965125/97866715-71d09f00-1d32-11eb-9a35-5418a5350422.png)
