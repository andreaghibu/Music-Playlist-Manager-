import string
def check_password_strength(password):
    criteria = []
    if len(password) < 8:
        criteria.append("Lungimea trebuie să fie de cel puțin 8 caractere.")

    if not any(char.isupper() for char in password):
        criteria.append("Trebuie să conțină cel puțin o literă majusculă.")

    if not any(char.islower() for char in password):
        criteria.append("Trebuie să conțină cel puțin o literă minusculă.")

    if not any(char.isdigit() for char in password):
        criteria.append("Trebuie să conțină cel puțin o cifră.")

    special_characters = "!@#$%^&*()-_+=<>?"
    if not any(char in special_characters for char in password):
        criteria.append(f"Trebuie să conțină cel puțin un caracter special ({special_characters}).")

    if any(char.isspace() for char in password):
        criteria.append("Nu trebuie să conțină spații.")

    return criteria
passwords_input = input("Introduceți parolele, separate prin virgulă: ")
passwords = [password.strip() for password in passwords_input.split(",")]
print("\nRezultatele verificării parolelor:")
for i, password in enumerate(passwords, 1):
    issues = check_password_strength(password)
    print(f"\nParola {i}: '{password}'")
    if not issues:
        print("  ✅ Parola este puternică!")
    else:
        print("  ❌ Parola este slabă. Probleme detectate:")
        for issue in issues:
            print(f"    - {issue}")

