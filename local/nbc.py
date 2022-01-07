import requests
import pandas as pd
import feedparser
from bs4 import BeautifulSoup
from requests.api import get

def getSoupObject(article_URL):
    page = requests.get(article_URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def getTextFromArticle_nbc(article_URL):
    entire_article = ''
    soup = getSoupObject(article_URL)
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs: 
        if "NBC" not in paragraph.text and "Sections" not in paragraph.text and "TV" not in paragraph.text and "Featured" not in paragraph.text and "tv" not in paragraph.text:
            entire_article += paragraph.text + ' '
            
    return entire_article

def getFeedContent(rss_url):
    feed = feedparser.parse(rss_url)
    feed_entries = feed.entries
    for entry in feed_entries:
        print(entry.link)

print(getTextFromArticle_nbc('https://www.nbcnews.com/news/world/new-variant-no-masks-driving-uks-latest-covid-surge-rcna3392'))
