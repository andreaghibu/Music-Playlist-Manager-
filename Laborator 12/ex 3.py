import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()
        prices = response.json()
        return [
            ["Bitcoin", prices["bitcoin"]["usd"]],
            ["Ethereum", prices["ethereum"]["usd"]]
        ]
    except requests.exceptions.RequestException:
        return "Eroare la obtinerea preturilor criptomonedelor."


def get_crypto_news():
    url = "https://www.coindesk.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("a", class_="headline", limit=5)
        news = [[article.text.strip(), url + article["href"]] for article in articles]
        return news
    except requests.exceptions.RequestException:
        return "Eroare la obtinerea stirilor despre criptomonede."


def main():
    print("Preturi actuale pentru criptomonede:")
    crypto_prices = get_crypto_prices()
    if isinstance(crypto_prices, list):
        print(tabulate(crypto_prices, headers=["Criptomoneda", "Pret (USD)"], tablefmt="grid"))
    else:
        print(crypto_prices)

    print("\nCele mai recente 5 stiri despre criptomonede:")
    crypto_news = get_crypto_news()
    if isinstance(crypto_news, list):
        print(tabulate(crypto_news, headers=["Titlu", "Link"], tablefmt="grid"))
    else:
        print(crypto_news)

if __name__ == "__main__":
    main()