import random
def number_guessing_game():
    numar_secret = random.randint(1, 100)
    incercari = 0

    print("Bine ai venit la Jocul de Ghicit Numere!")
    print("Am ales un număr între 1 și 100. Ghiceste-l!")

    while True:
        try:
            ghicit = int(input("Introdu numărul tău: "))
            incercari += 1

            if ghicit < numar_secret:
                print("Prea mic! Încearcă un număr mai mare.")
            elif ghicit > numar_secret:
                print("Prea mare! Încearcă un număr mai mic.")
            else:
                print(f"Felicitări! Ai ghicit numărul {numar_secret} în {incercari} încercări.")
                break
        except ValueError:
            print("Input invalid. Te rog să introduci un număr întreg.")
if __name__ == "__main__":
    number_guessing_game()
