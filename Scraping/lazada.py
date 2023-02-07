from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text=requests.get("https://www.lazada.sg/catalog/?_keyori=ss&from=input&q=mask").text
soup=BeautifulSoup(html_text,'lxml')
raw=soup.findAll('script')[3].text
page=pd.read_json(raw.split("window.pageData=")[1],orient='records')

