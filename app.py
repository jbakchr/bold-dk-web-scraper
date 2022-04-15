import sys
import requests
from bs4 import BeautifulSoup

args = sys.argv[1].lower()
url = "https://www.bold.dk/"

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

news_list_items = soup.find_all("div", {"class": "news_list_item"})

for news in news_list_items:
    headline = str(news.a.span.string)
    if args in headline.lower():
        link = f"https://bold.dk{news.a['href']}"
        print("*" * len(link))
        print(headline)
        print(link)
        print("*" * len(link), end="\n\n")
