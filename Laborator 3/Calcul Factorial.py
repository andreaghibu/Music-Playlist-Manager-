def calculeaza_factorial(numar):
    if numar < 0:
        return "Factorialul nu este definit pentru numere negative."
    elif numar == 0 or numar == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, numar + 1):
            factorial *= i
        return factorial

if __name__ == "__main__":
    try:
        numar = int(input("Introdu numărul pentru care vrei să calculezi factorialul: "))
        rezultat = calculeaza_factorial(numar)
        print(f"Factorialul lui {numar} este {rezultat}.")
    except ValueError:
        print("Te rog să introduci un număr întreg valid.")
