import numpy as np
import pandas as pd

np.random.seed(42)

num_days = 60
produs_min = 5
produs_max = 15
pret_medie = 40
deviatie_standard = 8
cantitate_min = 1
cantitate_max = 10
probabilitate_promotie = 0.3
reducere_promotie = 0.2
marja_profit = 0.3

zile = []
produse_vandute = []
preturi = []
cantitati = []
total_vanzari = []
profituri = []

for zi in range(num_days):

    numar_produs = np.random.randint(produs_min, produs_max + 1)
    produse_vandute.append(numar_produs)

    zi_promo = np.random.rand() < probabilitate_promotie
    pret_per_produs = np.random.normal(pret_medie, deviatie_standard)
    if zi_promo:
        pret_per_produs *= (1 - reducere_promotie)
    preturi.append(pret_per_produs)


    cantitate_per_produs = np.random.randint(cantitate_min, cantitate_max + 1, numar_produs)
    cantitati.append(cantitate_per_produs)

    total_per_zi = np.sum(pret_per_produs * cantitate_per_produs)
    total_vanzari.append(total_per_zi)

    profit_per_zi = total_per_zi * marja_profit
    profituri.append(profit_per_zi)

    zile.append(zi + 1)

df = pd.DataFrame({
    'Zi': zile,
    'Produse_vandute': produse_vandute,
    'Pret_unitar': preturi,
    'Cantitati_vandute': cantitati,
    'Total_vanzari': total_vanzari,
    'Profit': profituri
})

media_preturi = np.mean(preturi)
max_pret = np.max(preturi)
min_pret = np.min(preturi)

media_cantitati = np.mean([np.sum(cantitati_per_produs) for cantitati_per_produs in cantitati])
max_cantitate = np.max([np.sum(cantitati_per_produs) for cantitati_per_produs in cantitati])
min_cantitate = np.min([np.sum(cantitati_per_produs) for cantitati_per_produs in cantitati])

media_profit = np.mean(profituri)
max_profit = np.max(profituri)
min_profit = np.min(profituri)

total_vanzari_totale = np.sum(total_vanzari)
profit_total = np.sum(profituri)

print("Statistici generale:")
print(f"Media preturilor: {media_preturi:.2f}")
print(f"Maxim pret: {max_pret:.2f}, Min pret: {min_pret:.2f}")
print(f"Media cantităților vândute: {media_cantitati:.2f}")
print(f"Maxim cantitate vândută: {max_cantitate}, Min cantitate vândută: {min_cantitate}")
print(f"Media profitului: {media_profit:.2f}")
print(f"Maxim profit: {max_profit:.2f}, Min profit: {min_profit:.2f}")
print(f"Total vânzări pe întreaga perioadă: {total_vanzari_totale:.2f}")
print(f"Profit total pe întreaga perioadă: {profit_total:.2f}")

print("\nPrimele 5 zile din dataset:")
print(df.head())
