from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

print("hi, i am a smol scraper uwu.")
print("============================")
url = input("enter your site to scrape: (please enter http(s) in the beginning) ")
taggie = input("enter an html tag: (just the tag name) ")

def gettitle(url):
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html.read(), 'html.parser')
        tag = bs.find_all(taggie)
    except HTTPError as httperr: # http error function returns error codes (404, 401, etc) if urlopen throws an exception
        print(httperr)
    except URLError as urlerr: # url error function returns something like url not found if urlopen throws an exception
        print(urlerr)
    except AttributeError as tagerr:
        print("oh no. tag not found!")
    else:
        if tag == None:
            print("oh no. tag not found!")
        else:
            print(tag)

gettitle(url)