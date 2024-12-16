# Dicționar pentru prețuri și stocuri inițiale
produse_si_preturi = {"paine": 5.0, "lapte": 4.5, "oua": 0.8, "mere": 3.0, "faina": 2.5}
stoc_initial = {"paine": 10, "lapte": 20, "oua": 50, "mere": 8, "faina": 15}

# Listă de tupluri pentru vânzări
vanzari = [("paine", 3), ("lapte", 5), ("oua", 20), ("mere", 5), ("faina", 7)]

# Calculul veniturilor și actualizarea stocurilor
venit_total = 0
stoc_actualizat = stoc_initial.copy()
for produs, cantitate_vanduta in vanzari:
    if produs in produse_si_preturi:
        venit_total += produse_si_preturi[produs] * cantitate_vanduta
        stoc_actualizat[produs] -= cantitate_vanduta

# Produse cu stocuri scăzute
produse_de_realimentat = {produs for produs, cantitate in stoc_actualizat.items() if cantitate < 5}

# Raport final
print("\n=== RAPORT ZILNIC ===")
print(f"Venitul total din vânzări: {venit_total:.2f} lei")
print("\nStocuri rămase:")
for produs, cantitate in stoc_actualizat.items():
    print(f"  {produs}: {cantitate} bucăți")

print("\nProduse de realimentat:")
print("  Nu este nevoie de realimentare." if not produse_de_realimentat else "\n".join(f"  {produs}" for produs in produse_de_realimentat))
