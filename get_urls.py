from bs4 import BeautifulSoup
import urllib.request
import init

#* Start from the most recently chapter
with open(init.DEFAULT_URLS_FILE) as myfile:
    chapter_one = list(myfile)[-1]

#*
cur_chap = chapter_one
#! 'https://truyenfull.vn/legendary-moonlight-sculptor/quyen-1-chuong-1/' 
#! first chapter use for re-generate urls.txt file

#! with open(init.DEFAULT_URLS_FILE, 'a') as f:
#!         f.write(cur_chap)
#!         f.write("\n")
while True:
    page = urllib.request.urlopen(cur_chap)
    soup = BeautifulSoup(page, 'lxml')

    info = soup.find("a", {"id": "next_chap"})
    next_chap = info.get("href")
    if next_chap == "javascript:void(0)": #* If there no next chap then stop
        break
    cur_chap = next_chap
    with open(init.DEFAULT_URLS_FILE, 'a') as f:
        f.write(next_chap)
        f.write("\n")
