def filter_lines(input_file, output_file, keyword):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        filtered_lines = [line for line in lines if keyword in line]

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.writelines(filtered_lines)
        print(f"Fișierul filtrat a fost creat: {output_file}")
    except FileNotFoundError:
        print(f"Fișierul '{input_file}' nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")

input_file = "input ex 3.txt"
output_file = "filtered.txt"
keyword = "Python"
filter_lines(input_file, output_file, keyword)
