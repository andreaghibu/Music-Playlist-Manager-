import requests
import certifi

def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C\nTemperatura: %t\nVant: %w"
    try:
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError:
        return "Orasul nu a fost gasit."
    except requests.exceptions.RequestException:
        return "Eroare la conectarea la API."

def main():
    city = input("Introdu numele orasului: ").strip()
    weather_info = get_weather(city)
    print(f"\nVremea in {city}:\n{weather_info}")

if __name__ == "__main__":
    main()
