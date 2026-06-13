# utils/helpers.py
import requests

API_URL = "https://newsapi.org/v2/top-headlines"

def fetch_news_data(api_key, page_size, country_code=None, category=None, keyword=None):
    """
    Helper function to fetch news from NewsAPI.
    """
    params = {
        "apiKey": api_key,
        "pageSize": page_size
    }
    
    if country_code:
        params["country"] = country_code
    if category:
        params["category"] = category
    if keyword:
        params["q"] = keyword

    response = requests.get(API_URL, params=params)
    return response
