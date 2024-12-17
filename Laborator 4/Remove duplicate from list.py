def remove_duplicates():
    raw_input = input("Introdu elementele listei separate prin spațiu: ")
    items = raw_input.split()
    unique_items = list(dict.fromkeys(items))
    print("Lista fără duplicate este:", unique_items)
remove_duplicates()
