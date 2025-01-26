inventar = {}

def adauga_produs(nume, cantitate):
    try:
        cantitate = int(cantitate)
        if cantitate < 0:
            raise ValueError("Cantitatea nu poate fi negativă.")
        if nume in inventar:
            inventar[nume] += cantitate
        else:
            inventar[nume] = cantitate
        print(f"Produsul '{nume}' a fost adăugat cu succes.")
    except ValueError as e:
        print(f"Eroare: {e}")

def cauta_produs(nume):
    try:
        if nume in inventar:
            print(f"Produs: {nume}, Cantitate: {inventar[nume]}")
        else:
            raise KeyError(f"Produsul '{nume}' nu există în inventar.")
    except KeyError as e:
        print(e)

def actualizeaza_cantitate(nume, cantitate):
    try:
        cantitate = int(cantitate)
        if nume in inventar:
            inventar[nume] = cantitate
            print(f"Produsul '{nume}' a fost actualizat cu cantitatea: {cantitate}")
        else:
            raise KeyError(f"Produsul '{nume}' nu există în inventar.")
    except ValueError:
        print("Eroare: Cantitatea trebuie să fie un număr întreg.")
    except KeyError as e:
        print(e)

def afiseaza_meniu():
    print("\nSistem de Gestionare a Inventarului")
    print("1. Adaugă produs")
    print("2. Caută produs")
    print("3. Actualizează cantitatea produsului")
    print("4. Afișează inventarul complet")
    print("5. Ieșire")

# Loop principal
while True:
    afiseaza_meniu()
    optiune = input("Alegeți o opțiune: ")

    if optiune == "1":
        nume = input("Introduceți numele produsului: ")
        cantitate = input("Introduceți cantitatea: ")
        adauga_produs(nume, cantitate)

    elif optiune == "2":
        nume = input("Introduceți numele produsului pe care doriți să-l căutați: ")
        cauta_produs(nume)

    elif optiune == "3":
        nume = input("Introduceți numele produsului pe care doriți să-l actualizați: ")
        cantitate = input("Introduceți noua cantitate: ")
        actualizeaza_cantitate(nume, cantitate)

    elif optiune == "4":
        print("\nInventar complet:")
        if not inventar:
            print("Inventarul este gol.")
        else:
            for produs, cantitate in inventar.items():
                print(f"- {produs}: {cantitate} unități")

    elif optiune == "5":
        print("Ieșire din program. La revedere!")
        break

    else:
        print("Eroare: Opțiune invalidă. Vă rugăm să alegeți din meniu.")
