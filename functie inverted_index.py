def inverted_index(documents):
    """
    Creează un index inversat care asociază fiecărui cuvânt unic
    un set de indici ai documentelor în care apare acel cuvânt.

    Parametru:
    - documents: o listă de șiruri de caractere (fiecare șir reprezintă un document).

    Returnează:
    - Un dicționar unde cheile sunt cuvinte unice, iar valorile sunt seturi de indici.
    """
    index = {}

    for i, document in enumerate(documents):
        # Convertim documentul la litere mici și eliminăm semnele de punctuație
        clean_doc = document.lower().translate(str.maketrans("", "", string.punctuation))
        words = clean_doc.split()  # Împărțim documentul în cuvinte

        for word in words:
            if word not in index:
                index[word] = set()
            index[word].add(i)  # Adăugăm indexul documentului în set

    return index


# Solicităm utilizatorului să introducă lista de documente
import string

print("Introduceți documentele (fiecare document pe o linie). Tastați 'STOP' pentru a termina:")
documents = []
while True:
    line = input()
    if line.strip().lower() == "stop":
        break
    documents.append(line)

# Generăm indexul inversat
result = inverted_index(documents)

# Afișăm rezultatul
print("\nIndexul inversat este:")
for word, indices in result.items():
    print(f"{word}: {indices}")
