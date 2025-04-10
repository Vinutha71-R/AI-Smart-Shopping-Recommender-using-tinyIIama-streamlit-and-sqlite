import requests
from bs4 import BeautifulSoup

def scrape_amazon_search(query):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.amazon.in/s?k={query.replace(' ', '+')}"
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    for item in soup.select('.s-main-slot .s-result-item'):
        title = item.select_one('h2 span')
        price = item.select_one('.a-price-whole')

        if title and price:
            results.append({
                "title": title.text.strip(),
                "price": price.text.strip()
            })

    return results

# For testing
if __name__ == "__main__":
    products = scrape_amazon_search("headphones")
    for p in products:
        print(f"{p['title']} - ₹{p['price']}")
