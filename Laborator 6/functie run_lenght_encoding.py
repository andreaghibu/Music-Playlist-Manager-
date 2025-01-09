def run_length_encoding(text):
    if not text:
        return ""
    compressed = []
    current_char = text[0]
    count = 1

    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = char
            count = 1

    compressed.append(f"{current_char}{count}")
    return "".join(compressed)
text = input("Introdu un text: ")
output = run_length_encoding(text)
print(output)
