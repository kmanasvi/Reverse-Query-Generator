import ssl
import urllib.request
import nltk
from html.parser import HTMLParser 


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
    html=strip_tags(html)
    print (urls)


   

from nltk.corpus import wordnet as wn
#for synset in list(wn.all_synsets('v')):

