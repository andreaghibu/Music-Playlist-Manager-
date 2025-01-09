def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    result = " ".join(reversed_words)
    return result

sentence = input("Introdu o propoziție: ")
output = reverse_words(sentence)
print(output)
