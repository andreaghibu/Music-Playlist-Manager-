def genereaza_tabel_inmultire(numar, pana_la):
    print(f"Tabelul de înmulțire pentru {numar} (până la {pana_la}):")
    for i in range(1, pana_la + 1):
        print(f"{numar} x {i} = {numar * i}")
if __name__ == "__main__":
    try:
        numar = int(input("Introdu numărul pentru care dorești tabelul de înmulțire: "))
        pana_la = int(input("Introdu intervalul până la care să se genereze tabelul: "))

        genereaza_tabel_inmultire(numar, pana_la)
    except ValueError:
        print("Te rog să introduci valori întregi valide pentru număr și interval.")
