import urllib
import requests
import csv
from bs4 import BeautifulSoup


text_file=open("input.txt","r")
lines=text_file.readlines()
for line in range(0,len(lines)):
    u=lines[line]
    blog_page=u[:len(u)-1]
    page=requests.get(blog_page)
    page1=page.text
    soup=BeautifulSoup(page1,'html.parser')
    title=soup.find("h1",attrs={"class":"elevate-h1 u-marginBottom12 u-md-marginBottom8"})
    u=title.string
    print('Title: '+str(u).strip())
    subtitle=soup.find("p",attrs={"class":"elevate-summary u-md-marginBottom24"})
    t=subtitle.string
    print('Subtitle: '+str(t).strip())
    img_url=soup.find("div",attrs={"class":"elevateCover-image"})
    img_url=str(img_url)
    i=0
    while i < len(img_url):
        if(img_url[i]=='u' and img_url[i+1]=='r' and img_url[i+2]=='l'):
            s=i+4
        if(img_url[i]=='\"' and img_url[i+1]==')' and img_url[i+2]==';'):
            s1=i
            break;
        i=i+1
    img_url=str(img_url).strip()[s:s1+1]
    print('Image URL: '+str(img_url))
    date=soup.find("time",attrs={"class":"u-inlineBlock u-lineHeightBase"})
    date_f=date.string
    print('Date: '+str(date_f).strip())
    readTime=soup.find("span",attrs={"class":"readingTime"})
    readTime=str(readTime)
    i=0
    while i < len(readTime):
        if(readTime[i]=='m' and readTime[i+1]=='i' and readTime[i+2]=='n'):
            s2=i-2
            break
        i=i+1
    readTime=str(readTime).strip()[s2:i+3]
    print('Read Time: '+str(readTime).strip())
    author=soup.find("h3",attrs={"class":"ui-h2 u-paddingTop4 u-marginBottom4"})
    author_f=author.string
    print('Author: '+str(author_f).strip())
    aDesc=soup.find("p",attrs={"class":"ui-summary u-marginBottom16"})
    aDesc_f=aDesc.string
    print('Author Description: '+str(aDesc_f).strip())
    claps=soup.find("button",attrs={"class":"button button--chromeless u-baseColor--buttonNormal js-multirecommendCountButton u-textColorDarker","data-action":"show-recommends"})
    claps_f=claps.string
    print('No. of claps: '+str(claps_f).strip())
    content=soup.find("p",attrs={"class":"graf graf--p graf-after--p"})
    content_f=content.string
    with open('index.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([u,t,img_url,date_f,readTime,author_f,aDesc_f,claps_f])

text_file.close()
