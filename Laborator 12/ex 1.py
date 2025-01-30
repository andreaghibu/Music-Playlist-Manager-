import requests
from tabulate import tabulate

def get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Aruncă o eroare pentru status code >= 400
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Eroare la obținerea datelor: {e}")
        return []

def filter_users_by_city(users, city):
    return [user for user in users if user["address"]["city"] == city]


def display_users(users):
    if not users:
        print("Nu există utilizatori de afișat.")
        return

    table = []
    headers = ["ID", "Nume", "Username", "Email", "Oraș", "Companie", "Telefon", "Website"]

    for user in users:
        table.append([
            user["id"],
            user["name"],
            user["username"],
            user["email"],
            user["address"]["city"],
            user["company"]["name"],
            user["phone"],
            user["website"]
        ])

    print(tabulate(table, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    users = get_users()

    if users:
        print("\nToți utilizatorii:")
        display_users(users)

        city = "Gwenborough"
        print(f"\nUtilizatori din orașul {city}:")
        filtered_users = filter_users_by_city(users, city)
        display_users(filtered_users)
