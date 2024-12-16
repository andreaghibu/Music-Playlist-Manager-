def sistem_de_notare(punctaj):
    if 90 <= punctaj <= 100:
        return "A"
    elif 80 <= punctaj < 90:
        return "B"
    elif 70 <= punctaj < 80:
        return "C"
    elif 60 <= punctaj < 70:
        return "D"
    elif 0 <= punctaj < 60:
        return "F"
    else:
        return "Punctaj invalid"

def main():
    print(" Sistemul de Notare!")
    try:
        punctaj = float(input("Introdu punctajul studentului (0-100): "))
        nota = sistem_de_notare(punctaj)
        print(f"Nota pentru punctajul {punctaj} este: {nota}")
    except ValueError:
        print("Input invalid. Te rog să introduci un număr valid.")

if __name__ == "__main__":
    main()
