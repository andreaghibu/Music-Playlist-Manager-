class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"

if __name__ == "__main__":
    while True:
        print("\nAlege tipul de angajat pentru introducere:")
        print("1. Angajat")
        print("2. Manager")
        print("3. Ieșire")

        optiune = input("Introdu opțiunea ta: ")

        if optiune == "1":
            nume = input("Introdu numele angajatului: ")
            salariu = float(input("Introdu salariul angajatului: "))
            emp = Employee(nume, salariu)
            print(emp.get_details())
        elif optiune == "2":
            nume = input("Introdu numele managerului: ")
            salariu = float(input("Introdu salariul managerului: "))
            departament = input("Introdu departamentul managerului: ")
            mgr = Manager(nume, salariu, departament)
            print(mgr.get_details())
        elif optiune == "3":
            print("Ieșire. O zi bună!")
            break
        else:
            print("Opțiune invalidă. Te rog să încerci din nou.")
