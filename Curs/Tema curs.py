while True:
    caracter = input("Introduceti o litera: ")
    if len(caracter) == 1:
        if caracter.isalpha():
            print(f"Ai introdus litera: {caracter}")
        else:
            print("Eroare! Introduceti doar litere.")
            break
    else:
        print("Eroare! Introduceti doar un singur caracter.")
        break
