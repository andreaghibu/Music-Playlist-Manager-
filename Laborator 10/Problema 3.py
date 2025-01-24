class Produs:
    def __init__(self, nume, cantitate):
        self.nume = nume
        self.cantitate = cantitate

    def __str__(self):
        return f"{self.nume} - Cantitate: {self.cantitate}"


class Inventar:
    def __init__(self):
        self.produse = {}

    def adauga_produs(self, nume, cantitate):
        if nume in self.produse:
            print("Produsul există deja în inventar.")
        else:
            self.produse[nume] = Produs(nume, cantitate)
            print(f"Produsul '{nume}' a fost adăugat cu cantitatea {cantitate}.")

    def cauta_produs(self, nume):
        if nume in self.produse:
            print(self.produse[nume])
        else:
            print(f"Produsul '{nume}' nu a fost găsit în inventar.")

    def actualizeaza_cantitate(self, nume, cantitate):
        if nume in self.produse:
            self.produse[nume].cantitate = cantitate
            print(f"Cantitatea produsului '{nume}' a fost actualizată la {cantitate}.")
        else:
            print(f"Produsul '{nume}' nu a fost găsit în inventar.")


def meniu():
    inventar = Inventar()

    while True:
        print("\nMeniu:")
        print("1. Adaugă produs")
        print("2. Căutare produs")
        print("3. Actualizează cantitate")
        print("4. Ieși din program")

        try:
            optiune = int(input("Alege o opțiune: "))

            if optiune == 1:
                nume = input("Introdu numele produsului: ")
                try:
                    cantitate = int(input("Introdu cantitatea produsului: "))
                    if cantitate < 0:
                        print("Cantitatea nu poate fi negativă!")
                    else:
                        inventar.adauga_produs(nume, cantitate)
                except ValueError:
                    print("Eroare: Cantitatea trebuie să fie un număr întreg valid.")

            elif optiune == 2:
                nume = input("Introdu numele produsului de căutat: ")
                inventar.cauta_produs(nume)

            elif optiune == 3:
                nume = input("Introdu numele produsului pentru actualizare: ")
                try:
                    cantitate = int(input("Introdu noua cantitate: "))
                    if cantitate < 0:
                        print("Cantitatea nu poate fi negativă!")
                    else:
                        inventar.actualizeaza_cantitate(nume, cantitate)
                except ValueError:
                    print("Eroare: Cantitatea trebuie să fie un număr întreg valid.")

            elif optiune == 4:
                print("Ieșire din program.")
                break
            else:
                print("Opțiune invalidă, te rog alege din nou.")

        except ValueError:
            print("Eroare: Te rog să introduci un număr valid pentru opțiune.")


meniu()
