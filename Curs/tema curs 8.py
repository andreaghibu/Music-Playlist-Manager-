# Modulul: data_processor.py
import csv
def read_csv(file_path):
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def filter_data(data, key, value):
    return [row for row in data if row.get(key) == value]

def write_csv(data, file_path):
    if not data:
        raise ValueError("Datele de scris sunt goale.")

    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def input_csv_data():
    print("Introduceți datele pentru CSV (tastați 'stop' pentru a termina):")
    headers = input("Introduceți numele coloanelor, separate prin virgule: ").split(',')
    data = []

    while True:
        row_input = input("Introduceți valorile pentru un rând, separate prin virgule (sau 'stop'): ")
        if row_input.lower() == 'stop':
            break
        values = row_input.split(',')
        if len(values) != len(headers):
            print("Numărul de valori nu corespunde numărului de coloane. Încercați din nou.")
            continue
        row = dict(zip(headers, values))
        data.append(row)

    return data

if __name__ == "__main__":
    file_path = "people.csv"
    filtered_file_path = "filtered_people.csv"

    data = input_csv_data()
    print("Datele introduse:", data)

    write_csv(data, file_path)
    print(f"Datele introduse au fost scrise în {file_path}.")

    city = input("Introduceți orașul pentru care doriți să filtrați datele: ")
    filtered_data = filter_data(data, "City", city)
    print(f"Datele filtrate pentru orașul {city}:", filtered_data)

    write_csv(filtered_data, filtered_file_path)
    print(f"Datele filtrate au fost scrise în {filtered_file_path}.")

