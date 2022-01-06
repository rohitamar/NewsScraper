import requests
import pandas as pd
import feedparser
from bs4 import BeautifulSoup


def getSoupObject(article_URL):
    page = requests.get(article_URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def getTextFromArticle(article_URL):
    entire_article = ''
    soup = getSoupObject(article_URL)
    paragraphs = soup.find_all('div', {"class": "zn-body__paragraph"})
    for paragraph in paragraphs: 
        if "24/7 coverage" not in paragraph.text:
            entire_article += paragraph.text
    
    return entire_article

def getFeedContent(rss_url):
    feed = feedparser.parse(rss_url)
    feed_entries = feed.entries
    for entry in feed_entries:
        print(entry.link)

getFeedContent('http://rss.cnn.com/rss/cnn_topstories.rss')
getFeedContent('http://rss.cnn.com/rss/cnn_world.rss')
getFeedContent('http://rss.cnn.com/rss/cnn_us.rss')
getFeedContent('http://rss.cnn.com/rss/cnn_tech.rss')
getFeedContent('http://rss.cnn.com/rss/cnn_showbiz.rss')
getFeedContent('http://rss.cnn.com/rss/cnn_travel.rss')
