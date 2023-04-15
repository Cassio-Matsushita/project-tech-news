import re
from tech_news.database import db


# Requisito 7
def search_by_title(title):
    noticias = db.news.find({"title": {"$regex": title, "$options": "i"}})
    noticias_lista = [
        (noticia["title"], noticia["url"]) for noticia in noticias
    ]
    return noticias_lista


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):

    regex = re.escape(category)
    news = db.news.find({"category": {"$regex": regex, "$options": "i"}})
    return [(noticia["title"], noticia["url"]) for noticia in news]
