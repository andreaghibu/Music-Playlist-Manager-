def este_palindrom(text):
    text_curat = ''.join(char.lower() for char in text if char.isalnum())
    return text_curat == text_curat[::-1]

def main():
    print("Bine ai venit la Verificatorul de Palindrom!")
    text = input("Introdu textul pe care vrei să-l verifici: ")

    if este_palindrom(text):
        print(f"'{text}' este un palindrom!")
    else:
        print(f"'{text}' nu este un palindrom.")

if __name__ == "__main__":
    main()
