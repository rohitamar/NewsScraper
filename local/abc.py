import requests
import pandas as pd
import feedparser
from bs4 import BeautifulSoup

def getSoupObject(article_url):
    page = requests.get(article_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def getTextFromArticle(article_url):
    entire_article = ''
    soup = getSoupObject(article_url)
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        if(len(paragraph.text) < 10):
            break
        entire_article += paragraph.text.strip()
    
    return entire_article

def getFeedContent(rss_url):
    feed = feedparser.parse(rss_url)
    feed_entries = feed.entries
    for entry in feed_entries:
        print(entry.link)

getFeedContent('https://abcnews.go.com/abcnews/usheadlines')
getFeedContent('https://abcnews.go.com/abcnews/healthheadlines')
getFeedContent('https://abcnews.go.com/abcnews/technologyheadlines')
getFeedContent('https://abcnews.go.com/abcnews/entertainmentheadlines')
