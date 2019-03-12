import ssl
import urllib.request
import nltk
import fasttext
from html.parser import HTMLParser 

#https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

import ssl

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found")

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

query = "Geeksforgeeks"

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
  

for urls in search(query, tld='com', lang='en', num=1, start=0, stop=1, pause=2.0):
    response=urllib.request.urlopen(urls, context=ctx)
    html = response.read()
    html = html.decode("utf8")
    try: 
        from BeautifulSoup import BeautifulSoup
    except ImportError:
        from bs4 import BeautifulSoup
    parsed_html = BeautifulSoup(html,'html.parser')
    for script in parsed_html(["script", "style"]):
        script.extract()
    text = parsed_html.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk+" __label__" for chunk in chunks if chunk)
    f = open('data.txt','w+')
    f.write(str(text.encode('utf8')))

classifier = fasttext.supervised('data.txt', 'model',label_prefix='__label__')
result = classifier.test('data.txt')
print ('P@1:', result.precision)
print ('R@1:', result.recall)
print ('Number of examples:', result.nexamples)
