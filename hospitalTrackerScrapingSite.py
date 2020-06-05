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



'''<html lang="en">
   <head>
      <meta charset="utf-8">
      <link rel="icon" href="/favicon.ico">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      <meta name="theme-color" content="#000000">
      <link rel="manifest" href="/manifest.json">
      <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
      <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
      <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
      <link rel="mask-icon" href="/safari-pinned-tab.svg" color="#6c757d">
      <meta name="msapplication-TileColor" content="#2d89ef">
      <meta name="theme-color" content="#ffffff">
      <title>Coronavirus Outbreak in India - covid19india.org</title>
      <meta name="title" content="Coronavirus Outbreak in India: Latest Map and Case Count">
      <meta name="description" content="A volunteer-driven crowdsourced effort to track the coronavirus in India. A detailed country map shows the extent of the coronavirus outbreak, with tables of the number of cases by state and district.">
      <link rel="preconnect" href="https://www.google-analytics.com" crossorigin="">
      <link rel="preconnect" href="https://api.covid19india.org/v2/data.min.json">
      <link rel="preconnect" href="https://www.googletagmanager.com/" crossorigin="">
      <link rel="preload" importance="low" href="/fonts/Archia/archia-semibold-webfont.woff2" as="font" type="font/woff2" crossorigin="anonymous">
      <link rel="preload" importance="low" href="/fonts/Archia/archia-medium-webfont.woff2" as="font" type="font/woff2" crossorigin="anonymous">
      <link rel="preload" importance="low" href="/fonts/Archia/archia-bold-webfont.woff2" as="font" type="font/woff2" crossorigin="anonymous">
      <style>@font-face{font-family:Archia;src:url(/fonts/Archia/archia-semibold-webfont.eot);src:local('Archia'),url(/fonts/Archia/archia-semibold-webfont.eot?#iefix) format('embedded-opentype'),url(/fonts/Archia/archia-semibold-webfont.woff2) format('woff2'),url(/fonts/Archia/archia-semibold-webfont.woff) format('woff'),url(/fonts/Archia/archia-semibold-webfont.ttf) format('truetype');font-weight:600;font-style:normal;font-display:swap}@font-face{font-family:Archia;src:url(/fonts/Archia/archia-medium-webfont.eot);src:local('Archia'),url(/fonts/Archia/archia-medium-webfont.eot?#iefix) format('embedded-opentype'),url(/fonts/Archia/archia-medium-webfont.woff2) format('woff2'),url(/fonts/Archia/archia-medium-webfont.woff) format('woff'),url(/fonts/Archia/archia-medium-webfont.ttf) format('truetype');font-weight:400;font-style:normal;font-display:swap}@font-face{font-family:Archia;src:url(/fonts/Archia/archia-bold-webfont.eot);src:local('Archia'),url(/fonts/Archia/archia-bold-webfont.eot?#iefix) format('embedded-opentype'),url(/fonts/Archia/archia-bold-webfont.woff2) format('woff2'),url(/fonts/Archia/archia-bold-webfont.woff) format('woff'),url(/fonts/Archia/archia-bold-webfont.ttf) format('truetype');font-weight:900;font-style:normal;font-display:swap}</style>
      <meta property="og:type" content="website">
      <meta property="og:url" content="https://www.covid19india.org">
      <meta property="og:title" content="Coronavirus in India: Latest Map and Case Count">
      <meta property="og:description" content="A volunteer-driven crowdsourced effort to track the coronavirus in India. A detailed country map shows the extent of the coronavirus outbreak, with tables of the number of cases by state and district.">
      <meta property="og:image" content="https://www.covid19india.org/thumbnail.png">
      <meta property="og:image:type" content="image/png">
      <meta property="og:image:width" content="512">
      <meta property="og:image:height" content="512">
      <meta property="twitter:card" content="summary_large_image">
      <meta property="twitter:url" content="https://www.covid19india.org">
      <meta property="twitter:title" content="Coronavirus in India: Latest Map and Case Count">
      <meta name="twitter:site" value="@covid19indiaorg">
      <meta property="twitter:description" content="A volunteer-driven crowdsourced effort to track the coronavirus in India. A detailed country map shows the extent of the coronavirus outbreak, with tables of the number of cases by state and district.">
      <meta property="twitter:image" content="https://www.covid19india.org/thumbnail.png">
      <link href="/static/css/main.9d7fcf3d.chunk.css" rel="stylesheet">
   </head>
   <body class="light-mode">
      <noscript>You need to enable JavaScript to run this app.</noscript>
      <div id="root"></div>
      <script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script><script>!function(e){function t(t){for(var n,o,i=t[0],u=t[1],f=t[2],s=0,d=[];s<i.length;s++)o=i[s],Object.prototype.hasOwnProperty.call(a,o)&&a[o]&&d.push(a[o][0]),a[o]=0;for(n in u)Object.prototype.hasOwnProperty.call(u,n)&&(e[n]=u[n]);for(l&&l(t);d.length;)d.shift()();return c.push.apply(c,f||[]),r()}function r(){for(var e,t=0;t<c.length;t++){for(var r=c[t],n=!0,o=1;o<r.length;o++){var u=r[o];0!==a[u]&&(n=!1)}n&&(c.splice(t--,1),e=i(i.s=r[0]))}return e}var n={},o={9:0},a={9:0},c=[];function i(t){if(n[t])return n[t].exports;var r=n[t]={i:t,l:!1,exports:{}};return e[t].call(r.exports,r,r.exports,i),r.l=!0,r.exports}i.e=function(e){var t=[];o[e]?t.push(o[e]):0!==o[e]&&{11:1}[e]&&t.push(o[e]=new Promise((function(t,r){for(var n="static/css/"+({3:"About",4:"Demographics",5:"Essentials",6:"Home",7:"State"}[e]||e)+"."+{0:"31d6cfe0",1:"31d6cfe0",2:"31d6cfe0",3:"31d6cfe0",4:"31d6cfe0",5:"31d6cfe0",6:"31d6cfe0",7:"31d6cfe0",11:"93b3b32d",12:"31d6cfe0",13:"31d6cfe0"}[e]+".chunk.css",a=i.p+n,c=document.getElementsByTagName("link"),u=0;u<c.length;u++){var f=(l=c[u]).getAttribute("data-href")||l.getAttribute("href");if("stylesheet"===l.rel&&(f===n||f===a))return t()}var s=document.getElementsByTagName("style");for(u=0;u<s.length;u++){var l;if((f=(l=s[u]).getAttribute("data-href"))===n||f===a)return t()}var d=document.createElement("link");d.rel="stylesheet",d.type="text/css",d.onload=t,d.onerror=function(t){var n=t&&t.target&&t.target.src||a,c=new Error("Loading CSS chunk "+e+" failed.\n("+n+")");c.code="CSS_CHUNK_LOAD_FAILED",c.request=n,delete o[e],d.parentNode.removeChild(d),r(c)},d.href=a,document.getElementsByTagName("head")[0].appendChild(d)})).then((function(){o[e]=0})));var r=a[e];if(0!==r)if(r)t.push(r[2]);else{var n=new Promise((function(t,n){r=a[e]=[t,n]}));t.push(r[2]=n);var c,u=document.createElement("script");u.charset="utf-8",u.timeout=120,i.nc&&u.setAttribute("nonce",i.nc),u.src=function(e){return i.p+"static/js/"+({3:"About",4:"Demographics",5:"Essentials",6:"Home",7:"State"}[e]||e)+"."+{0:"6b427113",1:"52aecde1",2:"d596e359",3:"19126428",4:"fc11c277",5:"c2b1f9f7",6:"f57bbbab",7:"e5ae9869",11:"a7d3d8c8",12:"22968508",13:"26076852"}[e]+".chunk.js"}(e);var f=new Error;c=function(t){u.onerror=u.onload=null,clearTimeout(s);var r=a[e];if(0!==r){if(r){var n=t&&("load"===t.type?"missing":t.type),o=t&&t.target&&t.target.src;f.message="Loading chunk "+e+" failed.\n("+n+": "+o+")",f.name="ChunkLoadError",f.type=n,f.request=o,r[1](f)}a[e]=void 0}};var s=setTimeout((function(){c({type:"timeout",target:u})}),12e4);u.onerror=u.onload=c,document.head.appendChild(u)}return Promise.all(t)},i.m=e,i.c=n,i.d=function(e,t,r){i.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},i.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.t=function(e,t){if(1&t&&(e=i(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(i.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)i.d(r,n,function(t){return e[t]}.bind(null,n));return r},i.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return i.d(t,"a",t),t},i.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},i.p="/",i.oe=function(e){throw console.error(e),e};var u=this.webpackJsonpcovid19india=this.webpackJsonpcovid19india||[],f=u.push.bind(u);u.push=t,u=u.slice();for(var s=0;s<u.length;s++)t(u[s]);var l=f;r()}([])</script><script src="/static/js/10.f8629b82.chunk.js"></script><script src="/static/js/main.3c58d049.chunk.js"></script><script>!function(){function e(e){document.body.classList.add(e?"dark-mode":"light-mode"),document.body.classList.remove(e?"light-mode":"dark-mode")}var a=window.matchMedia("(prefers-color-scheme: dark)"),o="(prefers-color-scheme: dark)"===a.media,d=null;try{d=localStorage.getItem("darkMode")}catch(e){}var t=null!==d;if(t&&(d=JSON.parse(d)),t)e(d);else if(o)e(a.matches),localStorage.setItem("darkMode",a.matches);else{var r=document.body.classList.contains("dark-mode");localStorage.setItem("darkMode",JSON.stringify(r))}}()</script><script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-160698988-1"></script><script>function gtag(){dataLayer.push(arguments)}window.dataLayer=window.dataLayer||[],gtag("js",new Date),gtag("config","UA-160698988-1",{site_speed_sample_rate:1,sample_rate:1})</script>
   </body>
</html>
BODY IS:  [
<body class="light-mode">
   <noscript>You need to enable JavaScript to run this app.</noscript>
   <div id="root"></div>
   <script async="" src="https://www.google-analytics.com/analytics.js" type="text/javascript"></script><script>!function(e){function t(t){for(var n,o,i=t[0],u=t[1],f=t[2],s=0,d=[];s<i.length;s++)o=i[s],Object.prototype.hasOwnProperty.call(a,o)&&a[o]&&d.push(a[o][0]),a[o]=0;for(n in u)Object.prototype.hasOwnProperty.call(u,n)&&(e[n]=u[n]);for(l&&l(t);d.length;)d.shift()();return c.push.apply(c,f||[]),r()}function r(){for(var e,t=0;t<c.length;t++){for(var r=c[t],n=!0,o=1;o<r.length;o++){var u=r[o];0!==a[u]&&(n=!1)}n&&(c.splice(t--,1),e=i(i.s=r[0]))}return e}var n={},o={9:0},a={9:0},c=[];function i(t){if(n[t])return n[t].exports;var r=n[t]={i:t,l:!1,exports:{}};return e[t].call(r.exports,r,r.exports,i),r.l=!0,r.exports}i.e=function(e){var t=[];o[e]?t.push(o[e]):0!==o[e]&&{11:1}[e]&&t.push(o[e]=new Promise((function(t,r){for(var n="static/css/"+({3:"About",4:"Demographics",5:"Essentials",6:"Home",7:"State"}[e]||e)+"."+{0:"31d6cfe0",1:"31d6cfe0",2:"31d6cfe0",3:"31d6cfe0",4:"31d6cfe0",5:"31d6cfe0",6:"31d6cfe0",7:"31d6cfe0",11:"93b3b32d",12:"31d6cfe0",13:"31d6cfe0"}[e]+".chunk.css",a=i.p+n,c=document.getElementsByTagName("link"),u=0;u<c.length;u++){var f=(l=c[u]).getAttribute("data-href")||l.getAttribute("href");if("stylesheet"===l.rel&&(f===n||f===a))return t()}var s=document.getElementsByTagName("style");for(u=0;u<s.length;u++){var l;if((f=(l=s[u]).getAttribute("data-href"))===n||f===a)return t()}var d=document.createElement("link");d.rel="stylesheet",d.type="text/css",d.onload=t,d.onerror=function(t){var n=t&&t.target&&t.target.src||a,c=new Error("Loading CSS chunk "+e+" failed.\n("+n+")");c.code="CSS_CHUNK_LOAD_FAILED",c.request=n,delete o[e],d.parentNode.removeChild(d),r(c)},d.href=a,document.getElementsByTagName("head")[0].appendChild(d)})).then((function(){o[e]=0})));var r=a[e];if(0!==r)if(r)t.push(r[2]);else{var n=new Promise((function(t,n){r=a[e]=[t,n]}));t.push(r[2]=n);var c,u=document.createElement("script");u.charset="utf-8",u.timeout=120,i.nc&&u.setAttribute("nonce",i.nc),u.src=function(e){return i.p+"static/js/"+({3:"About",4:"Demographics",5:"Essentials",6:"Home",7:"State"}[e]||e)+"."+{0:"6b427113",1:"52aecde1",2:"d596e359",3:"19126428",4:"fc11c277",5:"c2b1f9f7",6:"f57bbbab",7:"e5ae9869",11:"a7d3d8c8",12:"22968508",13:"26076852"}[e]+".chunk.js"}(e);var f=new Error;c=function(t){u.onerror=u.onload=null,clearTimeout(s);var r=a[e];if(0!==r){if(r){var n=t&&("load"===t.type?"missing":t.type),o=t&&t.target&&t.target.src;f.message="Loading chunk "+e+" failed.\n("+n+": "+o+")",f.name="ChunkLoadError",f.type=n,f.request=o,r[1](f)}a[e]=void 0}};var s=setTimeout((function(){c({type:"timeout",target:u})}),12e4);u.onerror=u.onload=c,document.head.appendChild(u)}return Promise.all(t)},i.m=e,i.c=n,i.d=function(e,t,r){i.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},i.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.t=function(e,t){if(1&t&&(e=i(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(i.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)i.d(r,n,function(t){return e[t]}.bind(null,n));return r},i.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return i.d(t,"a",t),t},i.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},i.p="/",i.oe=function(e){throw console.error(e),e};var u=this.webpackJsonpcovid19india=this.webpackJsonpcovid19india||[],f=u.push.bind(u);u.push=t,u=u.slice();for(var s=0;s<u.length;s++)t(u[s]);var l=f;r()}([])</script><script src="/static/js/10.f8629b82.chunk.js"></script><script src="/static/js/main.3c58d049.chunk.js"></script><script>!function(){function e(e){document.body.classList.add(e?"dark-mode":"light-mode"),document.body.classList.remove(e?"light-mode":"dark-mode")}var a=window.matchMedia("(prefers-color-scheme: dark)"),o="(prefers-color-scheme: dark)"===a.media,d=null;try{d=localStorage.getItem("darkMode")}catch(e){}var t=null!==d;if(t&&(d=JSON.parse(d)),t)e(d);else if(o)e(a.matches),localStorage.setItem("darkMode",a.matches);else{var r=document.body.classList.contains("dark-mode");localStorage.setItem("darkMode",JSON.stringify(r))}}()</script><script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-160698988-1"></script><script>function gtag(){dataLayer.push(arguments)}window.dataLayer=window.dataLayer||[],gtag("js",new Date),gtag("config","UA-160698988-1",{site_speed_sample_rate:1,sample_rate:1})</script>
</body>
]'''