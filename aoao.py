import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://space.bilibili.com/122879/fans/fans"
response1 = urlopen(url).read()
print(response1)

soup = BeautifulSoup(response1, "html.parser", from_encoding="utf-8")
print(soup)
print(str(soup).replace(">", ">\n"))
print(soup.find_all('a'))
