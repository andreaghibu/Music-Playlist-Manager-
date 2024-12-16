def calculeaza_dobanda(credit, rate, timp):
    """
    Calculează dobânda pe baza formulei: dobanda = credit * rate * timp / 100

    :param credit: suma creditului (float)
    :param rate: rata dobânzii în procente (float)
    :param timp: perioada de timp în ani (float)
    :return: dobânda calculată (float)
    """
    dobanda = (credit * rate * timp) / 100
    return dobanda


# Exemplu de utilizare
try:
    credit = float(input("Introduceți suma creditului: "))
    rate = float(input("Introduceți rata dobânzii (în procente): "))
    timp = float(input("Introduceți perioada de timp (în ani): "))

    dobanda = calculeaza_dobanda(credit, rate, timp)
    print(f"Dobânda calculată este: {dobanda:.2f} unități monetare.")
except ValueError:
    print("Vă rugăm să introduceți valori numerice valide.")