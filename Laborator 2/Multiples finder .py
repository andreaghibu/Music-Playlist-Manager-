def gaseste_multipli(numar, limita):
    multipli = []
    for i in range(1, limita + 1):
        if i % numar == 0:
            multipli.append(i)
    return multipli

def main():
    print("Bine ai venit! Acest program găsește multipli ai unui număr.")
    try:
        numar = int(input("Introdu numărul: "))
        limita = int(input("Introdu limita până la care să găsim multipli: "))
        multipli = gaseste_multipli(numar, limita)
        print(f"Multiplii numărului {numar} până la {limita} sunt: {multipli}")
    except ValueError:
        print("Input invalid. Te rog să introduci numere întregi.")

if __name__ == "__main__":
    main()