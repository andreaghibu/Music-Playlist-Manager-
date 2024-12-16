def celsius_to_kelvin(celsius): return celsius + 273.15
valoare = float(input("Introduceti valoarea temperaturii: "))
unitate = input("Introduceti unitatea (C pentru Celsius): ").strip().upper()
if unitate == "C":  print(f"{valoare}° Celsius este {celsius_to_kelvin(valoare)} Kelvin.")
else: print("Unitate necunoscută! Programul acceptă doar Celsius.")
