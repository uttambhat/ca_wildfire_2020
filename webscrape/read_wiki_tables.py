import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from urllib.request import urlopen

url='https://en.wikipedia.org/w/index.php?title=2020_California_wildfires&oldid=973240987'
html = urlopen(url)
soup = BeautifulSoup(html,'html.parser')

tables = soup.find_all('table')

### string with commas to float ###
import re
def process_num(num):
    return float(re.sub(r'[^\w\s.]','',num))

#############
for table in tables:
    rows = table.find_all('tr')
    
    for row in rows:
        cells = row.find_all('td')
        
        
        if len(cells) > 1:
            rank = cells[0]
            ranks.append(int(rank.text))
            
            country = cells[1]
            countries.append(country.text.strip())
            
            rate = cells[2]
            rates.append(process_num(rate.text.strip()))

