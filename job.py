import requests
from bs4 import BeautifulSoup
import csv


job_description=[]
job_date=[]

#get data from site
result= requests.get("https://www.mourjan.com/sa/al-riyadh/programming/vacancies/")
page_content = result.content
#print(page_content)
soup=BeautifulSoup(page_content,"lxml")
#print(soup)

#job title job skills company name locations
job_title = soup.find_all("p",{"class":"ar"})

#get wanted text

for i in range(len(job_title)):
    job_description.append(job_title[i].text)
    #print(job_description[i])


#open file csv
with open("F:\COURSES\Projects\python\scrapping\jobs.csv","w",encoding="utf-8", mode='wb') as my_job:
    wr= csv.writer(my_job)
    wr.writerow(["jobs for programing"])
    wr.writerows(job_description)
