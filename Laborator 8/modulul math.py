import math
data = input("Introduceți numărul și unghiul, separate printr-un spațiu (ex: 25 30): ")
num, angle = map(float, data.split())

sqrt_num = math.sqrt(num)

factorial_num = math.factorial(int(num))

sin_angle = math.sin(math.radians(angle))

# Output
print(f"Rădăcina pătrată a {num} este {sqrt_num}")
print(f"Factorialul lui {int(num)} este {factorial_num}")
print(f"Sinusul unghiului de {angle} grade este {sin_angle}")
