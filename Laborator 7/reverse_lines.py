def reverse_lines(input_file, output_file):
    """
    Funcție care citește conținutul unui fișier și scrie într-un alt fișier
    fiecare rând inversat.

    :param input_file: Calea către fișierul de intrare
    :param output_file: Calea către fișierul de ieșire
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()  # Citește toate liniile din fișierul de intrare

        # Inversăm caracterele din fiecare linie
        reversed_lines = [line.rstrip()[::-1] for line in lines]

        with open(output_file, 'w', encoding='utf-8') as outfile:
            for reversed_line in reversed_lines:
                outfile.write(reversed_line + '\n')  # Scriem liniile inversate

        print(f"Fișierul inversat a fost creat: {output_file}")
    except FileNotFoundError:
        print(f"Fișierul '{input_file}' nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")

# Exemplu de utilizare
input_file = "input.txt"
output_file = "output.txt"
reverse_lines(input_file, output_file)
