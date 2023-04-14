import requests
import time
from bs4 import BeautifulSoup


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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
