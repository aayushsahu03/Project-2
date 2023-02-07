from bs4 import BeautifulSoup
import requests
def func1():
    with open("scraping/page.html","r") as html_file:
        content=html_file.read()
        soup=BeautifulSoup(content,'lxml')
        
        courses_html_tags=soup.find_all('h5') # searches for all tags with h5
        div_tags=soup.find_all('div',class_='card') # searches for all div tags with class="card"
        '''for course in courses_html_tags:
            print(course.text)
        '''
        for course in div_tags:
            p=course.a.text
            p=p[p.find("Rs"):]
            print(f"course name:{course.h5.text} for \t\t {p.ljust(15)}")

def func2():
    html_text=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python+developer&txtLocation=").text
    soup=BeautifulSoup(html_text,'lxml')
    div_tags=soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
    for job in div_tags:
        item=job.find('h3',class_='joblist-comp-name')
        skills=job.find('span',class_='srp-skills')
        print(f"comapnay name: {item.text.replace('(More Jobs)','').strip()}")
        print(f"skills       : {skills.text.replace(' ','').strip()}")
        print("="*50)
func2()