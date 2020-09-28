


import requests
import re
from bs4 import BeautifulSoup

def get_new_chapter():
  print("Is a new chapter at metruyenchu.com availablet yet?")
  url = input("Enter a link: ")
  while url == -1 or "metruyenchu.com/truyen" not in url:
    url = input("Invalid URL. Type again: ")
  # information for requests 
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"}
  details = {"title": "", "lastUpdated": ""}

  # start downloading
  page = requests.get(url, headers=headers)
  soup = BeautifulSoup(page.content, 'html5lib')
  # find title
  link = str(soup.find(href=re.compile("chuong")))
  titleFirstIndex = link.find("Chương")
  titleLastIndex = link.find("</a>")
  details["title"] = link[titleFirstIndex:titleLastIndex]
 
  # find last updated Time
  time = str(soup.find("div", class_="pl-3"))
  timeFirstIndex = time.find(">")
  timeLastIndex = time.find("</div>")
  details["lastUpdated"] = time[timeFirstIndex+1: timeLastIndex]
  
  # get chapter's content
  firstLinkIndex = link.find("https")
  lastLinkIndex = link.find(">")
  link = link[firstLinkIndex:lastLinkIndex-1]
  chapPage = requests.get(link, headers=headers)
  chapSoup = BeautifulSoup(chapPage.content, 'html5lib')
  text = str(chapSoup.find(id="js-read__content"))
  # remove extraneous details from the chapter
  firstEIndex = text.find("<div")
  lastEIndex = text.find(">", 2)
  text = text.replace(text[firstEIndex:lastEIndex+1], "")
  text = text.replace("<br/>", "")
  text = text.replace("</div>", "")

  return details

  
def main():
  print(get_new_chapter())

if __name__ == '__main__':
  main()