import string
def word_frequency(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency
text = "Acesta este un exemplu. Exemplul este simplu! Simplu și clar."
result = word_frequency(text)
print(result)
