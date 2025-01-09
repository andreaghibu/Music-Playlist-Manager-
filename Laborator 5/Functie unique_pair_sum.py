def unique_pair_sum(numbers, target):
    seen = set()
    pairs = set()

    for num in numbers:
        complement = target - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)

    return pairs

numbers_input = input("Introduceți numerele, separate prin spațiu: ")
numbers = list(map(int, numbers_input.split()))

target = int(input("Introduceți valoarea țintă: "))

result = unique_pair_sum(numbers, target)
print("Perechile unice care adunate dau valoarea țintă sunt:")
print(result)
