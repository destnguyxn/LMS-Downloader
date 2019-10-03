import get_content
import init

init.init()

with open(init.DEFAULT_URLS_FILE) as myfile:
    for url in list(myfile):
        get_content.get_content(url)

f = open(init.DEFAULT_HTML_FILE, 'a')
closed_tag = "\n</html>"
f.write(closed_tag)
f.close()
