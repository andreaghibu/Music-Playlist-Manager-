class Carte:
    def __init__(self, titlu, autor, ISBN):
        self.titlu = titlu
        self.autor = autor
        self.ISBN = ISBN
        self.este_imprumutata = False

    def __str__(self):
        status = "Împrumutată" if self.este_imprumutata else "Disponibilă"
        return f"{self.titlu} de {self.autor} (ISBN: {self.ISBN}) - {status}"


class MembruBiblioteca:
    def __init__(self, nume):
        self.nume = nume
        self.carti_imprumutate = []

    def imprumuta_carte(self, carte):
        if carte.este_imprumutata:
            print(f"Cartea '{carte.titlu}' este deja împrumutată.")
        else:
            carte.este_imprumutata = True
            self.carti_imprumutate.append(carte)
            print(f"{self.nume} a împrumutat cartea '{carte.titlu}'.")

    def returneaza_carte(self, carte):
        if carte in self.carti_imprumutate:
            carte.este_imprumutata = False
            self.carti_imprumutate.remove(carte)
            print(f"{self.nume} a returnat cartea '{carte.titlu}'.")
        else:
            print(f"{self.nume} nu a împrumutat cartea '{carte.titlu}'.")


class Biblioteca:
    def __init__(self):
        self.carti = []

    def adauga_carte(self, carte):
        self.carti.append(carte)
        print(f"Cartea '{carte.titlu}' a fost adăugată în bibliotecă.")

    def sterge_carte(self, carte):
        if carte in self.carti:
            self.carti.remove(carte)
            print(f"Cartea '{carte.titlu}' a fost ștearsă din bibliotecă.")
        else:
            print(f"Cartea '{carte.titlu}' nu există în bibliotecă.")

    def listeaza_carti_disponibile(self):
        print("Cărțile disponibile în bibliotecă:")
        for carte in self.carti:
            if not carte.este_imprumutata:
                print(f"  - {carte}")


# Exemplu de utilizare
biblioteca = Biblioteca()

# Introducerea cărților de la tastatură
numar_carti = int(input("Introduceți numărul de cărți de adăugat: "))
for _ in range(numar_carti):
    titlu = input("Introduceți titlul cărții: ")
    autor = input("Introduceți autorul cărții: ")
    ISBN = input("Introduceți ISBN-ul cărții: ")
    carte = Carte(titlu, autor, ISBN)
    biblioteca.adauga_carte(carte)

# Crearea membrilor bibliotecii de la tastatură
numar_membri = int(input("Introduceți numărul de membri de adăugat: "))
membri = []
for _ in range(numar_membri):
    nume = input("Introduceți numele membrului: ")
    membru = MembruBiblioteca(nume)
    membri.append(membru)

# Simulare interactivă
while True:
    print("\nMeniu:")
    print("1. Listează cărți disponibile")
    print("2. Împrumută carte")
    print("3. Returnează carte")
    print("4. Ieșire")
    optiune = input("Alegeți o opțiune: ")

    if optiune == "1":
        biblioteca.listeaza_carti_disponibile()
    elif optiune == "2":
        nume_membru = input("Introduceți numele membrului: ")
        titlu_carte = input("Introduceți titlul cărții: ")
        membru = next((m for m in membri if m.nume == nume_membru), None)
        carte = next((c for c in biblioteca.carti if c.titlu == titlu_carte), None)

        if membru and carte:
            membru.imprumuta_carte(carte)
        else:
            print("Membru sau carte invalidă.")
    elif optiune == "3":
        nume_membru = input("Introduceți numele membrului: ")
        titlu_carte = input("Introduceți titlul cărții: ")
        membru = next((m for m in membri if m.nume == nume_membru), None)
        carte = next((c for c in biblioteca.carti if c.titlu == titlu_carte), None)

        if membru and carte:
            membru.returneaza_carte(carte)
        else:
            print("Membru sau carte invalidă.")
    elif optiune == "4":
        print("La revedere!")
        break
    else:
        print("Opțiune invalidă. Încercați din nou.")

