import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from urllib.request import urlopen

url = 'http://delphimaster.net/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
req = requests.get(url, headers=headers)
print(r.status_code)
#url = 'http://delphimaster.net/'
#pag = urlopen(url)
#print(pag.read().decode('utf-8'))
