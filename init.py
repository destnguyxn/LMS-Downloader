DEFAULT_URLS_FILE = 'urls.txt'
DEFAULT_HTML_FILE = "LMS.html"

def init():
    f = open(DEFAULT_HTML_FILE, 'w+')

    head = """<?xml version='1.0' encoding='utf-8'?>
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Legendary Moonlight Sculptor - Con Đường Đế Vương</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <link href="stylesheet.css" rel="stylesheet" type="text/css"/>
    <link href="page_styles.css" rel="stylesheet" type="text/css"/>
    </head>\n"""

    f.write(head)
    f.close()
