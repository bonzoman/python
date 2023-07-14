import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

response = requests.get("https://library.gabia.com/")
soup = bs(response.text, "html.parser")
elements = soup.select('div.esg-entry-content a.eg-grant-element-0')


titles = []
links = []
for index, element in enumerate(elements, 1):
    titles.append(element.text)
    links.append(element.attrs['href'])
df = pd.DataFrame()
df['titles'] = titles
df['links'] = links

df.to_excel('./library_gabia.xlsx', sheet_name='Sheet1')
