# main.py
from geometry.circle import area as circle_area, circumference
from geometry.rectangle import area as rectangle_area, perimeter


def main():
    print("Bun venit! Alegeți tipul de calcul:")
    print("1. Cercul")
    print("2. Dreptunghiul")

    try:
        choice = int(input("Introduceți opțiunea (1 sau 2): "))

        if choice == 1:
            # Date pentru cerc
            radius = float(input("Introduceți raza cercului: "))
            print(f"Aria cercului este: {circle_area(radius):.2f}")
            print(f"Circumferința cercului este: {circumference(radius):.2f}")

        elif choice == 2:
            # Date pentru dreptunghi
            length = float(input("Introduceți lungimea dreptunghiului: "))
            width = float(input("Introduceți lățimea dreptunghiului: "))
            print(f"Aria dreptunghiului este: {rectangle_area(length, width):.2f}")
            print(f"Perimetrul dreptunghiului este: {perimeter(length, width):.2f}")

        else:
            print("Opțiunea introdusă nu este validă.")

    except ValueError:
        print("Ați introdus valori nevalide. Vă rugăm să introduceți numere.")
    except Exception as e:
        print(f"Eroare neașteptată: {e}")


if __name__ == "__main__":
    main()
