# main_script.py
import math_operations

def main():
    print("Operații disponibile:")
    print("1. Adunare")
    print("2. Scădere")
    print("3. Înmulțire")
    print("4. Împărțire")

    try:
        # Alegerea operației
        choice = int(input("Alege operația (1-4): "))
        if choice not in [1, 2, 3, 4]:
            raise ValueError("Operația aleasă nu este validă.")

        # Introducerea numerelor
        a = float(input("Introduce primul număr: "))
        b = float(input("Introduce al doilea număr: "))

        # Calcularea rezultatului în funcție de alegere
        if choice == 1:
            result = math_operations.add(a, b)
        elif choice == 2:
            result = math_operations.subtract(a, b)
        elif choice == 3:
            result = math_operations.multiply(a, b)
        elif choice == 4:
            result = math_operations.divide(a, b)

        print(f"Rezultatul este: {result}")

    except ValueError as e:
        print(f"Eroare: {e}")
    except Exception as e:
        print(f"Eroare neașteptată: {e}")

if __name__ == "__main__":
    main()
4