def nu_este_prim(numar):
    # Numerele mai mici decât 2 nu sunt prime
    if numar < 2:
        return True
    # Verificăm dacă numărul are alți divizori în afară de 1 și el însuși
    for i in range(2, int(numar**0.5) + 1):  # Verificăm până la rădăcina pătrată a numărului
        if numar % i == 0:
            return True
    return False
# Verificăm mai multe numere
numere= [1, 2, 3, 4, 5, 16, 17, 18, 19, 20]
for n in numere:
    if nu_este_prim(n):
        print(f"{n} NU este un număr prim.")
    else:
        print(f"{n} este un număr prim.")
