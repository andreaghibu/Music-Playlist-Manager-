import os
def citeste_filme():
    filme = {}
    if os.path.exists("movies.txt"):
        with open("movies.txt", "r") as f:
            for linie in f.readlines():
                titlu, evaluare = linie.strip().split(", ")
                filme[titlu] = int(evaluare)
    return filme

def salveaza_filme(filme):
    with open("movies.txt", "w") as f:
        for titlu, evaluare in filme.items():
            f.write(f"{titlu}, {evaluare}\n")

def vizualizeaza_filme(filme):
    if not filme:
        print("Nu sunt filme înregistrate.")
    else:
        filme_sortate = sorted(filme.items(), key=lambda x: x[1], reverse=True)
        for titlu, evaluare in filme_sortate:
            print(f"{titlu} - Evaluare: {evaluare}")

def adauga_film(filme):
    titlu = input("Introduceti titlul filmului: ")
    while True:
        try:
            evaluare = int(input("Introduceti evaluarea (1-5): "))
            if 1 <= evaluare <= 5:
                break
            else:
                print("Evaluarea trebuie sa fie intre 1 si 5.")
        except ValueError:
            print("Evaluarea trebuie sa fie un numar intreg.")
    filme[titlu] = evaluare
    print(f"Film adaugat: {titlu} cu evaluarea {evaluare}")

def actualizeaza_evaluare(filme):
    titlu = input("Introduceti titlul filmului pe care doriti sa il actualizati: ")
    if titlu in filme:
        while True:
            try:
                evaluare = int(input("Introduceti noua evaluare (1-5): "))
                if 1 <= evaluare <= 5:
                    filme[titlu] = evaluare
                    print(f"Evaluarea filmului '{titlu}' a fost actualizata la {evaluare}")
                    break
                else:
                    print("Evaluarea trebuie sa fie intre 1 si 5.")
            except ValueError:
                print("Evaluarea trebuie sa fie un numar intreg.")
    else:
        print(f"Film cu titlul '{titlu}' nu exista.")

def sterge_film(filme):
    titlu = input("Introduceti titlul filmului pe care doriti sa il stergeti: ")
    if titlu in filme:
        del filme[titlu]
        print(f"Film '{titlu}' sters cu succes.")
    else:
        print(f"Film cu titlul '{titlu}' nu exista.")

def sistem_evaluare_filme():
    filme = citeste_filme()

    while True:
        print("\nMeniu:")
        print("1. Vizualizează toate filmele și evaluările acestora")
        print("2. Adaugă un nou film")
        print("3. Actualizează evaluarea unui film existent")
        print("4. Șterge un film")
        print("5. Salvează modificările și iesi")
        alegere = input("Alege o opțiune (1-5): ")

        if alegere == "1":
            vizualizeaza_filme(filme)
        elif alegere == "2":
            adauga_film(filme)
        elif alegere == "3":
            actualizeaza_evaluare(filme)
        elif alegere == "4":
            sterge_film(filme)
        elif alegere == "5":
            salveaza_filme(filme)
            print("Modificările au fost salvate. La revedere!")
            break
        else:
            print("Opțiune invalidă. Vă rugăm să alegeți o opțiune între 1 și 5.")

if __name__ == "__main__":
    sistem_evaluare_filme()
