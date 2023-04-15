import requests
import time
import re
from bs4 import BeautifulSoup
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    try:
        time.sleep(1)
        html_content = requests.get(url, headers=headers, timeout=3)
        if html_content.status_code != 200:
            return None

    except requests.ReadTimeout:
        return None
    return html_content.text


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    links = []
    for link in soup.find_all(class_="cs-overlay-link"):
        href = link.get("href")
        links.append(href)
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    next_page_url = soup.find(class_="next page-numbers")
    if next_page_url:
        return next_page_url.get("href")
    return None


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    item = {}

    link_element = soup.find("link", rel="canonical")
    item["url"] = link_element.get("href")

    item["title"] = soup.find(class_="entry-title").string.rstrip()
    item["timestamp"] = soup.find(class_="meta-date").string
    item["writer"] = soup.find(class_="url fn n").string

    reading_time = soup.find(class_="meta-reading-time").get_text()
    reading_time_number = re.search(r"\d+", reading_time)
    if reading_time_number:
        item["reading_time"] = int(reading_time_number.group())

    item["summary"] = (
        soup.find("div", class_="entry-content").find("p").get_text().rstrip()
    )
    item["category"] = soup.find(class_="label").string

    return item


# Requisito 5
def get_tech_news(amount):
    news_links_list = []
    news_list = []
    url = "https://blog.betrybe.com/"

    htlml_content = fetch(url)
    news_links_list = scrape_updates(htlml_content)

    while amount > len(news_links_list):
        if amount < len(news_links_list):
            break
        url = scrape_next_page_link(htlml_content)
        htlml_content = fetch(url)
        news_links_list += scrape_updates(htlml_content)

    for news in news_links_list:
        htlml_content = fetch(news)
        news_list.append(scrape_news(htlml_content))
    create_news(news_list[:amount])

    return news_list[:amount]
