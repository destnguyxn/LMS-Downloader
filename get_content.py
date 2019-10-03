from bs4 import BeautifulSoup
import urllib.request
import re
from os.path import basename, splitext
import init

prev_book_number = -1
cur_book_number = 0

def get_content(url):
    global prev_book_number, cur_book_number
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'lxml')

    info = soup.find("a", {"class": "chapter-title"})
    content = soup.find("div", {"id": "chapter-c"})
    title = info.get('title')
    cur_book_number = title.split()[10]
    seperator = ' '
    chapter_title = seperator.join(title.split()[12:])
    #* ----- Download image to local and change the source
    for img in content.findAll('img'):
        link = img['src']
        filename = link.split('/')[-1]
        urllib.request.urlretrieve(link , filename)
        img['src'] = filename
    f = open(init.DEFAULT_HTML_FILE, 'a')
    #* ----- Process content
    if cur_book_number != prev_book_number:
        body = """<body>
    <h1>Quyển {0}</h1>
</body>\n""".format(cur_book_number)
        f.write(body)
    prev_book_number = cur_book_number
    body = """<body>
    <h2>{0}</h2>
    {1}
</body>\n""".format(chapter_title, content)

    f.write(body)
    f.close()
