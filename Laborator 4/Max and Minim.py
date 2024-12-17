def find_max_min():

    raw_input = input("Introdu numerele separate prin spațiu: ")
    numbers = list(map(float, raw_input.split()))

    if not numbers:
        print("Nu ai introdus niciun număr.")
        return

    maximum = max(numbers)
    minimum = min(numbers)

    print(f"Valoarea maximă este: {maximum}")
    print(f"Valoarea minimă este: {minimum}")

find_max_min()
