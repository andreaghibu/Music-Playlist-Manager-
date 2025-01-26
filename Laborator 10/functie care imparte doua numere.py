def imparte_numere(a, b):
    try:
        rezultat = a / b
        return f"Rezultatul împărțirii este: {rezultat}"
    except ZeroDivisionError:
        return "Eroare: Împărțirea la zero nu este permisă."

numar1 = float(input("Introduceți primul număr: "))
numar2 = float(input("Introduceți al doilea număr: "))

print(imparte_numere(numar1, numar2))
