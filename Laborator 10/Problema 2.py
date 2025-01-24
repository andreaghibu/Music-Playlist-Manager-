def citeste_si_suma(fisier):
    try:
        with open(fisier, 'r') as f:
            suma = 0
            for linie in f:
                try:
                    numar = float(linie.strip())
                    suma += numar
                except ValueError:
                    print(f"Atenție: Linia '{linie.strip()}' nu este un număr valid.")
            return suma
    except FileNotFoundError:
        return "Eroare: Fișierul nu a fost găsit."
    except IOError:
        return "Eroare: Nu s-a putut citi fișierul."

# Introducem numele fișierului de la tastatură
fisier = input("Introduceți numele fișierului: ")

# Apelăm funcția pentru a calcula suma numerelor din fișier
rezultatul = citeste_si_suma(fisier)
print("Rezultatul sumei este:", rezultatul)
