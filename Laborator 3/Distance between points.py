def distanta_dintre_puncte(x1, y1, x2, y2):
    from math import sqrt
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if __name__ == "__main__":
    try:
        x1 = float(input("Introdu coordonata x pentru primul punct: "))
        y1 = float(input("Introdu coordonata y pentru primul punct: "))
        x2 = float(input("Introdu coordonata x pentru al doilea punct: "))
        y2 = float(input("Introdu coordonata y pentru al doilea punct: "))

        distanta = distanta_dintre_puncte(x1, y1, x2, y2)
        print(f"Distanța dintre punctele ({x1}, {y1}) și ({x2}, {y2}) este {distanta:.2f}.")
    except ValueError:
        print("Te rog să introduci valori numerice valide pentru coordonate.")