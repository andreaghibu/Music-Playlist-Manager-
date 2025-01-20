def count_words_in_file(file_path):
    """
    Funcție care citește conținutul unui fișier text și returnează numărul total de cuvinte.

    :param file_path: Calea către fișierul text
    :return: Numărul total de cuvinte din fișier
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()         # Citește conținutul fișierului
            words = content.split()      # Împarte textul în cuvinte
            return len(words)            # Returnează numărul de cuvinte
    except FileNotFoundError:
        print(f"Fișierul '{file_path}' nu a fost găsit.")
        return 0
    except Exception as e:
        print(f"A apărut o eroare: {e}")
        return 0

# Exemplu de utilizare
file_path = "example.txt"  # Numele fișierului text
num_words = count_words_in_file(file_path)
print(f"Numărul total de cuvinte din '{file_path}' este: {num_words}")
