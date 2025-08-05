import requests
from bs4 import BeautifulSoup

def fetch_html(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def extract_titles(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.select("h3 a")
    return [a.get_text(strip=True) for a in articles if a.get_text(strip=True)]
