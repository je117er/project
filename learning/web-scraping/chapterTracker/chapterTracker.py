'''
    File name: chapterTracker.py
    Description: This program finds the latest chapter of
    of a story on metruyenchu.com and download it to local dir.
    Author: jd
    First created: 9/28/2020
    Last modified: 9/28/2020
    Usage: $ python3 chapterTracker.py
'''

import requests
import re
from bs4 import BeautifulSoup


# find range of substring
def range_find(text, s1, s2, i=1, j=1):
    firstIndex = text.find(s1, i)
    lastIndex = text.find(s2, j)
    return firstIndex, lastIndex


def get_chapter_number(title):
    number = ""
    for s in title:
        if (s.isdigit()): number += s
    return number

# find new chapter's information and download to local
def get_new_chapter():
  print("Tìm chương mới trên metruyenchu.com ...")
  url = input("Nhập link: ")
  while url == -1 or "metruyenchu.com/truyen" not in url:
      url = input("Link không hợp lệ. Vui lòng nhập lại: ")

  # information for requests
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"}
  details = {"title": "", "lastUpdated": ""}

  # start downloading html file
  page = requests.get(url, headers=headers)
  soup = BeautifulSoup(page.content, 'html5lib')

  # find title
  link = str(soup.find(href=re.compile("chuong")))
  titleFirstIndex, titleLastIndex = range_find(link, "Chương", "</a>")
  details["title"] = link[titleFirstIndex:titleLastIndex]

  # find last updated Time
  time = str(soup.find("div", class_="pl-3"))
  timeFirstIndex, timeLastIndex = range_find(time, ">", "</div>")
  details["lastUpdated"] = time[timeFirstIndex+1: timeLastIndex]

  # print chapter's info
  print("Chương mới nhất trên server: {}. Cập nhật lần cuối lúc: {}.".format(details["title"], details["lastUpdated"]))

  # file format: chuong-number.txt
  title = details["title"]
  chapterNumber = get_chapter_number(title)
  chapter_name = 'chuong-' + chapterNumber + '.txt'
  # check if file already exists
  try:
      with open(chapter_name) as f:
          print("Chương {} đã tồn tại trong thư mục.".format(chapterNumber))
  # if not, download it
  except IOError:
      print("Chương {} chưa tồn tại trong thư mục.".format(chapterNumber))
      print("Chuẩn bị download chương {}...".format(chapterNumber))
      get_chapter_content(link, title, chapter_name, headers)
      print("Chương {} đã được download thành công!".format(chapterNumber))


# download chapter's contents
def get_chapter_content(link, title, chapter_name, headers):
  # get link to new chapter
  firstLinkIndex, lastLinkIndex = range_find(link, "https", ">")
  link = link[firstLinkIndex:lastLinkIndex-1]

  # now connect to new chapter's link
  chapPage = requests.get(link, headers=headers)
  chapSoup = BeautifulSoup(chapPage.content, 'html5lib')
  text = str(chapSoup.find(id="js-read__content"))

  # remove extraneous details from the chapter
  firstEIndex, lastEIndex = range_find(text, "div", ">")
  extra = text[firstEIndex-1: lastEIndex+1]
  text = text.replace(extra, "")
  text = text.replace("<br/>", "")
  text = text.replace("</div>", "")

  # add title to chapter's contents
  text = title + '\n' + text

  # now write to a new file
  with open(chapter_name, 'w') as f:
      f.write(text)


def main():
  get_new_chapter()


# driver code
if __name__ == '__main__':
  main()
