def imparte(numar1, numar2):
    try:
        rezultat = numar1 / numar2
        return rezultat
    except ZeroDivisionError:
        return "Eroare: Împărțirea la zero nu este permisă!"

try:
    numar1 = float(input("Introduceți primul număr: "))
    numar2 = float(input("Introduceți al doilea număr: "))

    # Afișăm rezultatul
    print("Rezultatul împărțirii este:", imparte(numar1, numar2))
except ValueError:
    print("Eroare: Trebuie să introduceți doar numere valide!")
