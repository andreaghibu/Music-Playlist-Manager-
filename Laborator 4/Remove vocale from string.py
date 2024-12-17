def remove_vowels():
    text = input("Introduceți un șir de caractere: ")
    vowels = "aeiouăâîAEIOUĂÂÎ"
    result = "".join([char for char in text if char not in vowels])
    print("Șirul fără vocale este:", result)
remove_vowels()
