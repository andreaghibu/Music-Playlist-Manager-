def verifica_paritate(numar):
    if numar % 2 == 0:
        return "par"
    else:
        return "impar"

try:
    numar = int(input("Introduceți un număr: "))
    rezultat = verifica_paritate(numar)
    print(f"Numărul {numar} este {rezultat}.")
except ValueError:
    print("Vă rugăm să introduceți un număr valid!")