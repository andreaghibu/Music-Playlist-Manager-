import csv

def process_csv(input_file, output_file):
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            fieldnames = ['Produs', 'Cantitate', 'Pret unitar', 'Valoare totala']

            with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    try:
                        cantitate = int(row['Cantitate'])
                        pret_unitar = float(row['Pret unitar'])
                        valoare_totala = cantitate * pret_unitar
                        row['Valoare totala'] = round(valoare_totala, 2)
                        writer.writerow(row)
                    except ValueError:
                        print(f"Eroare la conversie pentru linia: {row}")
        print("Procesare finalizată cu succes.")
    except FileNotFoundError:
        print("Fișierul specificat nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")


def main():
    input_file = input("Introduceți calea către fișierul CSV de intrare: ").strip()
    output_file = input("Introduceți calea pentru fișierul CSV de ieșire: ").strip()
    process_csv(input_file, output_file)


if __name__ == "__main__":
    main()
