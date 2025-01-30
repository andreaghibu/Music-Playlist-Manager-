import requests
# Funcția pentru a obține cursurile de schimb de la API
def obtine_cursuri_de_schimb():
    url = "https://api.exchangerate.host/latest"  # URL-ul API-ului pentru cursurile de schimb
    response = requests.get(url)  # Se trimite cererea GET la API

    if response.status_code == 200:  # Verificăm dacă răspunsul a fost OK
        data = response.json()  # Obținem răspunsul JSON

        # Verificăm dacă cheia 'rates' există în răspuns
        if 'rates' in data:
            return data['rates']  # Extragem cursurile de schimb din răspunsul JSON
        else:
            print("Cheia 'rates' nu a fost găsită în răspunsul API!")
            print("Răspunsul complet:", data)  # Afișăm răspunsul complet pentru depanare
            return None
    else:
        print("Eroare la obținerea cursurilor de schimb! Status:", response.status_code)
        return None


# Funcția pentru a efectua conversia între două monede
def convertește_monede(cursuri_de_schimb, moneda_inceput, moneda_destinatie, suma):
    if moneda_inceput == 'EUR':
        curs_de_schimb = cursuri_de_schimb.get(moneda_destinatie)
        if curs_de_schimb:
            return suma * curs_de_schimb  # Calculăm suma convertită
        else:
            print("Moneda de destinație nu este validă!")
            return None
    else:
        # Dacă moneda de început nu este EUR, o vom transforma mai întâi în EUR
        curs_in_eur = cursuri_de_schimb.get(moneda_inceput)
        curs_de_schimb = cursuri_de_schimb.get(moneda_destinatie)

        if curs_in_eur and curs_de_schimb:
            suma_in_eur = suma / curs_in_eur  # Transformăm suma în EUR
            return suma_in_eur * curs_de_schimb  # Calculăm suma finală
        else:
            print("Moneda de start sau moneda de destinație nu sunt valide!")
            return None


# Funcția principală pentru rularea programului
def main():
    cursuri_de_schimb = obtine_cursuri_de_schimb()  # Obținem cursurile de schimb

    if cursuri_de_schimb:
        moneda_inceput = input("Introduceți moneda de proveniență (de exemplu, RON, USD, EUR): ").upper()
        moneda_destinatie = input("Introduceți moneda de destinație (de exemplu, RON, EUR, USD): ").upper()
        suma = float(input("Introduceți suma pe care doriți să o convertească: "))

        suma_convertita = convertește_monede(cursuri_de_schimb, moneda_inceput, moneda_destinatie, suma)

        if suma_convertita is not None:
            curs_in_eur = cursuri_de_schimb.get(moneda_inceput, 1)  # Dacă moneda de început este EUR, cursul e 1
            curs_destinatie = cursuri_de_schimb.get(moneda_destinatie, 1)

            print(f"\nRezultatul conversiei:")
            print(f"Suma inițială: {suma} {moneda_inceput}")
            print(f"Cursul de schimb {moneda_inceput} la {moneda_destinatie}: {curs_destinatie / curs_in_eur:.2f}")
            print(f"Suma finală: {suma_convertita:.2f} {moneda_destinatie}")
        else:
            print("Conversia nu a fost posibilă.")


if __name__ == '__main__':
    main()
