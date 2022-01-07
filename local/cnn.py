import requests
import pandas as pd
import feedparser

from bs4 import BeautifulSoup

RSS_URLS = [
    'http://rss.cnn.com/rss/cnn_topstories.rss',
    'http://rss.cnn.com/rss/cnn_travel.rss',
    'http://rss.cnn.com/rss/cnn_world.rss',
    'http://rss.cnn.com/rss/cnn_us.rss',
    'http://rss.cnn.com/rss/cnn_tech.rss',
    'http://rss.cnn.com/rss/cnn_showbiz.rss'
]

TEST_CNN_URLS = [
    'https://www.cnn.com/2022/01/06/politics/january-6-anniversary/index.html',
    'https://www.cnn.com/2022/01/06/politics/joe-biden-january-6-speech-anniversary/index.html',
    'https://www.cnn.com/2022/01/06/motorsport/dakar-rally-blast-terrorism-probe-intl-spt/index.html',
    'https://www.cnn.com/2021/12/31/business/hong-kong-cathay-pacific-flight-suspension-intl-hnk/index.html',
    'https://www.cnn.com/2022/01/06/tech/social-media-january-6-anniversary/index.html',
    'https://www.cnn.com/travel/article/airline-passengers-partying-canada-sunwing/index.html'
]

def get_soup_object(article_url):
    """
    article_url: the URL of the article
    """
    page = requests.get(article_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def get_headline(soup_object, travel):
    """
    soup_object: a BeautifulSoup object of the article URL
    travel: boolean to represent whether an article has genre Travel
    """
    h1_tag = soup_object.find_all('h1', {"class": "Article__title"}) if travel else soup_object.find_all('h1', {"class": "pg-headline"})
    if(len(h1_tag) > 0):
        return h1_tag[0].text

def get_first_paragraph(soup_object):
    """
    soup_object: a BeautifulSoup object of the article URL
    """
    first_paragraph = soup_object.find('p', {"class": "zn-body__paragraph"})
    return first_paragraph.text

def get_last_paragraph(soup_object):
    """
    soup_object: a BeautifulSoup object of the article URL
    """
    paragraphs = soup_object.find_all('div', {"class": "zn-body__paragraph"})
    return paragraphs[len(paragraphs)-2].text

def get_first_last_paragraph_travel(soup_object):
    """
    soup_object: a BeautifulSoup object of the article URL
    """
    paragraphs = soup_object.find_all('div', {"class": "Paragraph__component"})
    return paragraphs[0].span.text, paragraphs[len(paragraphs)-2].span.text

def get_article_info(article_url):
    """
    article_url: the URL of the article
    """
    soup = get_soup_object(article_url)
    article_info = {}
    travel = 'travel' in article_url
    article_info['headline'] = get_headline(soup, travel)
    if travel:
        article_info['first_paragraph'], article_info['last_paragraph'] = get_first_last_paragraph_travel(soup)
    else:
        article_info['first_paragraph'] = get_first_paragraph(soup)
        article_info['last_paragraph'] = get_last_paragraph(soup)
    return article_info

def process_feed(rss_url):
    """
    rss_url: the url of the rss feed
    """
    feed = feedparser.parse(rss_url)
    feed_entries = feed.entries
    for entry in feed_entries:
        get_article_info(entry.link)

def tests():
    for URL in TEST_CNN_URLS:
        article = get_article_info(URL)
        print(article)
    
if __name__ == "__main__":
    tests()

