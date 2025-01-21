class ContBancar:
    def __init__(self, sold_initial=0):

        self._sold = sold_initial

    def depune(self, suma):

        if suma > 0:
            self._sold += suma
            print(f"Depus: {suma}. Sold nou: {self._sold}")
        else:
            print("Suma de depus trebuie să fie pozitivă.")

    def retrage(self, suma):

        if suma > 0:
            if suma <= self._sold:
                self._sold -= suma
                print(f"Retras: {suma}. Sold rămas: {self._sold}")
            else:
                print("Fonduri insuficiente.")
        else:
            print("Suma de retras trebuie să fie pozitivă.")

    def obtine_sold(self):

        return self._sold
if __name__ == "__main__":
    sold_initial = float(input("Introdu soldul inițial pentru cont: "))
    cont = ContBancar(sold_initial=sold_initial)

    while True:
        print("\nAlege o opțiune:")
        print("1. Verifică soldul")
        print("2. Depune bani")
        print("3. Retrage bani")
        print("4. Ieșire")

        optiune = input("Introdu opțiunea ta: ")

        if optiune == "1":
            print(f"Sold curent: {cont.obtine_sold()}")
        elif optiune == "2":
            suma = float(input("Introdu suma de depus: "))
            cont.depune(suma)
        elif optiune == "3":
            suma = float(input("Introdu suma de retras: "))
            cont.retrage(suma)
        elif optiune == "4":
            print("Ieșire. O zi bună!")
            break
        else:
            print("Opțiune invalidă. Te rog să încerci din nou.")